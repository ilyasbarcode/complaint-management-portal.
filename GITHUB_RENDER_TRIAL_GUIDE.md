# GitHub + Render trial deployment (v0.2.4)

## What goes where
- GitHub repository: source code and version history. Create a **Private** repository named `complaint-management-portal`.
- Render: deploys the Django website from GitHub and provides a temporary `onrender.com` URL.
- Render PostgreSQL: database provisioned by `render.yaml`. Current code has no complaint data models yet, so it is only the framework database at this stage.

## Upload to GitHub using a laptop browser
1. Download and extract this ZIP.
2. Open the extracted `complaint_portal_starter` folder. The files inside it (`manage.py`, `requirements.txt`, `render.yaml`, `build.sh`, `config/`, `apps/`, `templates/`, `static/`) must be at the **top level of the GitHub repository**. Do not upload the outer ZIP as one file.
3. On GitHub, create a new **Private** repository named `complaint-management-portal`; do not initialize it with a README or other files.
4. Open the empty repository, choose **Add file → Upload files**, and upload the contents of `complaint_portal_starter` (not the parent folder and not the ZIP). Commit to `main`.
5. Do not upload real complaint/customer CSV or Excel exports. The sample-derived schemas and blank template are already included.

## Deploy on Render
1. Sign in to Render and authorize GitHub access to the private repository.
2. Choose **New → Blueprint** (or Blueprint Instance), select `complaint-management-portal`, and apply the `render.yaml` configuration.
3. Render reads `render.yaml`, builds the Django app, collects static files, runs migrations, and starts Gunicorn. Wait for the deploy to finish.
4. Open the Render service URL ending in `.onrender.com`.

## Expected trial result
The Dashboard landing page should appear with the ComplaintCare sidebar and project cards. The other sidebar entries are intentionally marked Planned and are not functional yet. This is a visual foundation trial, not an operational complaint system.

## Important trial limitations
- Do not upload real customer/complaint data.
- No complaint models, live upload page/import, status workflow, approvals, live reports, or MC generator exist yet.
- Render free web services can sleep after inactivity; the first visit after sleeping may take time. Free services are for trial, not guaranteed production availability.
- Keep repository private. Never commit `.env`, secrets, database URLs, real customer exports, phone numbers, addresses, or attachment URLs.
- For later updates, edit code, commit/push to `main`; Render can automatically redeploy from the connected branch.

## Local laptop preview (no GitHub required)
From the extracted `complaint_portal_starter` folder in Windows PowerShell:

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

Open `http://127.0.0.1:8000/`. Stop with `Ctrl+C`.
