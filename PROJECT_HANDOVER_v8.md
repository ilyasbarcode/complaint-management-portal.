# Complaint Management Portal — Project Handover v8.0

**Date:** 15 November 2026  
**Code package:** v0.2.3  
**Status:** Django starter, confirmed input/output schemas, sample Work Done reference values, and upload workbook structure validator. This is not a completed complaint portal.

## 1. Project objective
Develop an independent, professional, responsive, multi-user complaint management portal by observing the existing portal through authorized normal-user access. No admin/backend/database/source access or bypass is assumed.

## 2. Newly confirmed Upload Complaint input
The user confirmed that the Upload Complaint Excel file has exactly 13 columns, in this exact order:

| # | Header |
|---:|---|
| 1 | S.No |
| 2 | CRMID |
| 3 | Notification No |
| 4 | Order No |
| 5 | Equipment No |
| 6 | Distributor |
| 7 | Customer Name |
| 8 | Phone No |
| 9 | Address |
| 10 | City Name |
| 11 | Remarks |
| 12 | Territory |
| 13 | Ref. Type |

A blank workbook is included at `templates/Upload_Complaint_Template.xlsx`. `apps/core/upload_schema.py` validates exact header spelling/order on the first worksheet and reads non-empty rows. This is a structural validator only: it does not create database records or connect to a portal upload screen.

Not yet confirmed: mandatory/optional fields, duplicate rules, file-size limits, allowed sheet names, accepted date/number formats, row-level error handling, and what status/action follows upload. These must not be guessed.

## 3. Confirmed non-MC exports
The supplied `complaints.csv` is an export sample with 714 rows and 47 columns. The user confirmed that all non-MC Excel downloads use the same 47-column layout, including All Complaints, pending lists, Vendor Approval, Pending CCI Approval, Master Data 2025/2026 and Batch Export. The exact schema is in `apps/core/export_schemas.py`. Sample customer data and personal contact details are not bundled in the code package.

## 4. Confirmed MC export
The supplied MC sample has 356 rows and 8 columns in this order: `CRMID`, `Notification`, `Order No`, `materialCode`, `materialDescription`, `Qty`, `Warranty`, `Resolve date`. MC is line-item based: one row per material/part used, so an Order No may repeat. Existing `materialCode` values are present and must be preserved; no separate material-code mapping file is required based on the user's clarification. MC is generated in the backend and downloaded as Excel; it is not a detailed line-item portal screen. Filters observed: reporting year, start date, end date, optional territory and optional order numbers.

## 5. Work Done remarks
The supplied complaints export contains 47 distinct non-empty combined `Work Done` strings. They are preserved verbatim in `apps/core/work_done_standards.py`, including capitalization, commas and spacing. This is a sample-derived list, not proof that all technician-app options have been captured. The technician application remains the source of the standard remarks.

## 6. Other observed portal areas
Navigation observed: Dashboard, All Complaint, Upload Complaint, Pending CCI Approval, Master Data 2026, MC, Export and Master Data 2025. Batch Export accepts Order Numbers, Notification Numbers and CRM IDs. Pending CCI Approval includes selection controls, Excel export and a feedback modal with “Send back Vendor” and “Approved”; actual status transitions have not been verified. Dashboard charts/metrics were observed at a point in time and are not fixed requirements.

## 7. Current code implementation
Included:
- Django project foundation and responsive dashboard shell.
- PostgreSQL Docker Compose service definition and SQLite quick-preview option.
- Shared 47-column non-MC export schema and 8-column MC schema.
- XLSX column selection/writer helpers (not connected to live portal data).
- 47 sample-derived Work Done strings and tests.
- 13-column Upload Complaint schema, blank Excel template, workbook header validator/row reader and tests.

Not implemented:
- Complaint models, database persistence, create/edit/assign/resolve workflow.
- Upload Complaint web screen and database import transaction.
- CCI approval state transitions and vendor feedback workflow.
- Technician-app integration.
- Live database-backed exports, MC generation/filtering and master-data workflows.
- Production user roles/permissions, audit trail, deployment hardening and backups.

## 8. Windows laptop execution (development preview)
Requires Python 3.14 and internet access for package installation.

1. Extract the ZIP archive.
2. Open PowerShell inside the `complaint_portal_starter` folder (the folder containing `manage.py`).
3. Create and activate the virtual environment:
   ```powershell
   py -3.14 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   If activation is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that PowerShell window, then activate again.
4. Install requirements:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Select SQLite for a local preview:
   ```powershell
   $env:DB_ENGINE = "sqlite"
   $env:DJANGO_DEBUG = "1"
   ```
6. Check and initialize the database:
   ```powershell
   python manage.py check
   python manage.py migrate
   ```
7. Start the development server:
   ```powershell
   python manage.py runserver
   ```
8. Open `http://127.0.0.1:8000/` in the laptop browser. Stop with `Ctrl+C`.

Run automated tests with `python manage.py test`. This remains a development starter; only the dashboard shell is a portal page at this stage. The Upload Complaint validator is a reusable code module, not a functioning upload page.

### PostgreSQL option
Install Docker Desktop and run `docker compose up -d db`. Set `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST=localhost`, and `POSTGRES_PORT=5432` in the same PowerShell session, and do not set `DB_ENGINE=sqlite`. Then run migrations and the development server. Docker Compose starts PostgreSQL only; Django runs locally.

## 9. Privacy and production cautions
Do not bundle real complaint/customer exports in source packages. Before real use, implement authentication and role-based permissions, validate uploads safely, protect personal information and attachment URLs, configure secrets/HTTPS/allowed hosts, backups, logging and deployment infrastructure. Django's development server is not for production.

## 10. Next development stage
Implement database models and connect the validated 13-column upload to a controlled import workflow after confirming field-level validation and duplicate/error behavior. Then implement complaint lifecycle, approval actions, exports and MC generation against verified rules.
