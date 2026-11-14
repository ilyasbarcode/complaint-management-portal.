"""Safe MC workflow primitives.

MC is eligible only after CCI approval. Material extraction is driven by explicit
aliases configured in the Material Master, not by guessing from arbitrary text.
"""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

@dataclass(frozen=True)
class MaterialRule:
    material_code: str
    material_description: str
    aliases: tuple[str, ...]
    default_qty: str | None = None
    warranty: str | None = None

class MCWorkflowError(ValueError):
    pass

def is_cci_approved(status: str) -> bool:
    return str(status or "").strip().casefold() in {"approved", "cci approved"}

def select_materials_from_work_done(work_done: str, rules: list[MaterialRule]):
    """Return exact alias matches in Work Done, preserving master-list order.

    Generic service phrases are not interpreted as physical materials unless
    explicitly configured as an alias. Issue is contextual only and is not parsed
    as a material list.
    """
    text = str(work_done or "").casefold()
    selected = []
    seen = set()
    for rule in rules:
        if not rule.material_code or not rule.material_description:
            continue
        aliases = rule.aliases or (rule.material_description,)
        matched = any(alias.strip() and alias.casefold() in text for alias in aliases)
        if matched and rule.material_code not in seen:
            selected.append(rule)
            seen.add(rule.material_code)
    return selected

def build_mc_rows(complaint: dict, rules: list[MaterialRule]):
    """Build sample-compatible 8-column MC rows for one approved complaint.

    Quantity and Warranty are not guessed. Each selected material needs configured
    values or an upstream technician-app value before an export row can be emitted.
    """
    if not is_cci_approved(complaint.get("Status")):
        raise MCWorkflowError("MC can only be generated after CCI approval.")
    selected = select_materials_from_work_done(complaint.get("Work Done", ""), rules)
    rows = []
    for rule in selected:
        if rule.default_qty in (None, "") or rule.warranty in (None, ""):
            raise MCWorkflowError(
                f"Quantity/Warranty rule is missing for material {rule.material_code}."
            )
        try:
            qty = Decimal(str(rule.default_qty))
        except InvalidOperation:
            raise MCWorkflowError(f"Invalid quantity for material {rule.material_code}.")
        rows.append({
            "CRMID": complaint.get("CRMID", ""),
            "Notification": complaint.get("Notification No", ""),
            "Order No": complaint.get("Order No", ""),
            "materialCode": rule.material_code,
            "materialDescription": rule.material_description,
            "Qty": qty,
            "Warranty": rule.warranty,
            "Resolve date": complaint.get("Resolved Date", ""),
        })
    if not rows:
        raise MCWorkflowError("No configured material matched Work Done; manual review required.")
    return rows
