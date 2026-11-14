# Project Handover — Complaint Management Portal
Version 9.0 | 15 November 2026

## Project purpose
Independent rebuild of the complaint management portal using confirmed user-provided formats and normal-user observations. This package is a development foundation with verified schemas and selected domain logic; it is not a completed production system.

## Current technical foundation
- Python 3.14 target
- Django 6.1.3
- PostgreSQL for deployment
- Pandas/OpenPyXL for spreadsheet processing
- Gunicorn + WhiteNoise for Render deployment
- Docker Compose PostgreSQL option for local development

## Confirmed workflow
1. Complaints arrive through the 13-column Upload Complaint Excel template.
2. Complaint resolution includes standardized `Issue` and `Work Done` remarks integrated from technician application.
3. Technicians select parts/actions in their application; selected parts/actions appear in Work Done.
4. Complaint enters Pending CCI Approval.
5. When CCI approves, the complaint becomes eligible for MC.
6. MC logic interprets Work Done against verified Material Master aliases; exact code and description are copied.
7. Each selected material becomes one MC row; Order No repeats for multiple materials.
8. MC download uses the exact 8-column sample schema.
9. Other exports use the same 47-column schema.

## Exact data schemas
### Upload Complaint — 13 columns
S.No | CRMID | Notification No | Order No | Equipment No | Distributor | Customer Name | Phone No | Address | City Name | Remarks | Territory | Ref. Type

### Shared non-MC export — 47 columns
The exact ordered schema is in `apps/core/export_schemas.py`. All Complaints, Pending, Vendor Approval, Pending CCI Approval, Master Data 2025/2026 and Batch Export share this schema.

### MC — 8 columns
CRMID | Notification | Order No | materialCode | materialDescription | Qty | Warranty | Resolve date

MC sample inspected: 356 rows, 8 columns. It is line-item based; multiple materials for one order create multiple rows with repeated Order No.

## Technician remarks
- User supplied screenshots of an Excel with `Issue` and `Work Done` columns.
- These are standard technician-app remarks, not free-text phrases.
- Work Done includes selected part/action names combined into one remark.
- The supplied complaints.csv has 714 rows, 47 columns and 47 distinct non-empty Work Done values.
- Sample strings are preserved in `apps/core/work_done_standards.py`.
- They are not guaranteed to be the full technician-app option list.
- Future technician-app video is expected to verify the close workflow and source values.

## Material Master status
A Material Master List was shown as an image in earlier discussion. The actual complete machine-readable file is not currently part of this repository. Do not infer or hardcode codes from an incomplete screenshot. Import authoritative master list and define verified aliases before turning on automated MC export.

## Implemented in v0.3.0
- Django starter and responsive dashboard shell.
- Upload Complaint 13-column header schema, workbook validator, blank template generator and tests.
- Shared 47-column non-MC schema and MC 8-column schema.
- Export schema ordering helpers.
- 47 sample-derived Work Done strings.
- MC workflow guard: approval-only gate, explicit material alias matching, missing Qty/Warranty error, unmatched selection review error.
- GitHub/Render configuration from previous starter retained.
- Requirements and handover documentation updated.

## Not implemented / must not be represented as complete
- Persistent Complaint database models and full CRUD.
- Live upload page, transaction, duplicate policy and database import.
- Complete All Complaints filters/detail/attachments and pagination.
- CCI approval screen, state transitions, role enforcement and audit log.
- Complete material master import/maintenance and full alias table.
- Technician app connector or part/quantity/warranty feed.
- Production MC query and download action.
- Batch Export query and download action.
- Complete Admin Panel, roles, user management and production hardening.

## Required business decisions / inputs
1. Upload duplicate behavior (CRMID and/or Order No): reject, skip or update.
2. Required upload fields and value validation.
3. CCI status transitions and approval authority.
4. Full Material Master workbook/list with exact codes and descriptions.
5. Qty and Warranty source/rules.
6. Technician app video of selecting parts and closing complaint.
7. Roles/permissions.
8. Attachment storage/access/retention rules.

## Local run — Windows PowerShell
From the folder containing `manage.py`:
```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:DB_ENGINE = "sqlite"
$env:DJANGO_DEBUG = "1"
python manage.py check
python manage.py migrate
python manage.py runserver
```
Open `http://127.0.0.1:8000/`. Stop with Ctrl+C. Run tests with `python manage.py test`.
For a real multi-user trial, configure PostgreSQL. Do not use SQLite or Django's development server for production.

## GitHub upload
1. Download and extract ZIP.
2. Open the extracted `complaint_portal_starter` folder.
3. Create a **Private** GitHub repository named `complaint-management-portal`.
4. Upload the *contents* of this folder to the repository root (not the outer folder and not the ZIP).
5. Confirm `manage.py`, `requirements.txt`, `render.yaml`, `config/`, `apps/` and `docs/` are at repository root.
6. Commit changes. Do not upload `.env`, database files, customer data or secrets.

## Render trial
1. Sign in to Render and connect GitHub.
2. Choose New → Blueprint and select the repository.
3. Apply `render.yaml`; set a strong `DJANGO_SECRET_KEY` if prompted/needed.
4. Wait for build and migration to finish, then open the Render URL.
5. Check logs and run a smoke test. Public deployment must not contain real customer data until authentication, roles and data protection are complete.

## GitHub repository checklist
- README.md
- requirements.txt
- .gitignore
- render.yaml / Dockerfile / build.sh
- config/
- apps/core/
- templates/ and static/
- docs/REQUIREMENTS_v1.md
- docs/PROJECT_HANDOVER_v9.md

## Version statement
v0.3.0 is a GitHub-ready development foundation, not a complete functional portal. The next development milestone is database-backed Upload Complaint + All Complaints + CCI Approval, followed by Material Master and MC once mapping/Qty/Warranty rules are verified.
