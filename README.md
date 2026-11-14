# Complaint Management Portal — Repository v0.3.0

**Status:** GitHub-ready development foundation; not a completed production portal.

## Start here
- `docs/REQUIREMENTS_v1.md` — consolidated requirements and acceptance criteria.
- `docs/PROJECT_HANDOVER_v9.md` — complete handover, confirmed workflows, setup and deployment.
- `apps/core/requirements_status.md` — implemented vs pending status.

## Confirmed schemas
- Upload Complaint: 13 columns.
- All non-MC downloads: shared 47 columns.
- MC: 8 columns; one row per material and repeated Order No.

## Local quick start (Windows PowerShell)
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
Open `http://127.0.0.1:8000/`. Run `python manage.py test`.

## GitHub
Create a **Private** repository named `complaint-management-portal`. Upload the contents of this folder (not the ZIP itself) to the repository root. Keep secrets and customer data out of GitHub.

## Render
Use New → Blueprint and select the GitHub repository. Render reads `render.yaml`. Follow `GITHUB_RENDER_TRIAL_GUIDE.md`.

## Important
The upload validator currently validates the confirmed workbook structure; it is not yet a database import workflow. MC service logic requires verified material aliases plus Qty/Warranty rules. Do not enable automatic production MC until those are supplied.
