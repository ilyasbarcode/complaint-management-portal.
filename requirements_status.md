# Implementation status — v0.3.0

This repository is a development-ready foundation, not a production-complete portal.
Implemented and tested:
- Django starter and responsive dashboard shell.
- Confirmed 13-column Upload Complaint workbook header validator/template.
- Confirmed 47-column shared non-MC export schema and 8-column MC schema.
- Sample Work Done strings retained from the provided 714-row export sample (47 distinct values).
- Pure-Python MC workflow guard: only CCI-approved complaints qualify; exact configured aliases in Work Done can select materials; missing Qty/Warranty or unmatched material raises a review error.

Not yet implemented:
- Complaint database persistence, duplicate policy, full upload UI/import transaction.
- Complete All Complaints search/filter/detail/attachment experience.
- CCI approval UI, role permissions and transactional status/audit workflow.
- Material master data import and verified alias mapping from technician-app selections.
- Technician app integration or automatic retrieval of part IDs/quantities/warranty.
- Production MC query and export button, with confirmed Qty/Warranty derivation.
- Batch Export data query, authentication/roles, production security hardening.

The 32-ish material entries previously shown in a screenshot are not embedded as a verified machine-readable master list in this repository. Import the authoritative material master workbook/list before enabling automatic MC export.
