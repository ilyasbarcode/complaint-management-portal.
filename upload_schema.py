"""Confirmed Upload Complaint Excel input schema and safe workbook validation."""
from pathlib import Path
from copy import copy
from openpyxl import load_workbook, Workbook

UPLOAD_COMPLAINT_COLUMNS = (
    "S.No", "CRMID", "Notification No", "Order No", "Equipment No",
    "Distributor", "Customer Name", "Phone No", "Address", "City Name",
    "Remarks", "Territory", "Ref. Type",
)


def validate_upload_complaint_workbook(source):
    """Validate the first worksheet header row and return structured row data.

    Accepts a path or a seekable binary file object. This validates only the
    confirmed 13-column structure; business-required fields and value rules
    remain unconfirmed and are deliberately not invented here.
    """
    workbook = load_workbook(source, read_only=True, data_only=True)
    try:
        if not workbook.worksheets:
            raise ValueError("Workbook has no worksheets.")
        sheet = workbook.worksheets[0]
        header = tuple(cell.value for cell in next(sheet.iter_rows(min_row=1, max_row=1)))
        if header != UPLOAD_COMPLAINT_COLUMNS:
            raise ValueError(
                "Upload Complaint headers do not match the confirmed 13-column "
                f"format. Expected: {list(UPLOAD_COMPLAINT_COLUMNS)}; found: {list(header)}"
            )
        rows = []
        for values in sheet.iter_rows(min_row=2, values_only=True):
            padded = tuple(values[:len(UPLOAD_COMPLAINT_COLUMNS)])
            if len(padded) < len(UPLOAD_COMPLAINT_COLUMNS):
                padded += (None,) * (len(UPLOAD_COMPLAINT_COLUMNS) - len(padded))
            if not any(value not in (None, "") for value in padded):
                continue
            rows.append(dict(zip(UPLOAD_COMPLAINT_COLUMNS, padded)))
        return rows
    finally:
        workbook.close()


def create_upload_complaint_template(destination):
    """Create a blank .xlsx template with the exact confirmed header order."""
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Upload Complaint"
    sheet.append(list(UPLOAD_COMPLAINT_COLUMNS))
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = f"A1:M1"
    for cell in sheet[1]:
        font = copy(cell.font)
        font.bold = True
        cell.font = font
    workbook.save(destination)
    return Path(destination)
