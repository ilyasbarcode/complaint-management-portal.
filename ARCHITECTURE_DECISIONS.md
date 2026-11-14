# Architecture Decisions — 14 November 2026

## Decision 001 — Django application framework
Selected Django 6.1.3 as the current supported Django feature release at the project baseline date. It supports Python 3.12–3.15; this starter targets Python 3.14 for a stable supported runtime. Django provides authentication, sessions, admin foundations, ORM, migrations, CSRF protection and mature server-rendered application support.

## Decision 002 — PostgreSQL database
Selected PostgreSQL 18.7, a supported production major release at the baseline date. PostgreSQL 19 was still a release candidate on the baseline date and is not selected for production.

## Decision 003 — Modular monolith first
Start as a modular Django monolith. Separate apps can be introduced for complaints, master data, approvals, materials, MC reporting, exports, audit and users after requirements are confirmed. Avoid premature microservices.

## Decision 004 — Excel handling
Use OpenPyXL for workbook-level reading/writing and Pandas only where tabular transformations are useful. Never guess the original upload template or MC export schema.

## Decision 005 — UI
Use responsive HTML/CSS templates initially. The supplied dashboard is only a design foundation, not a reproduction of the original portal or a finished workflow.

## Production requirements still open
Choose hosting, object/file storage, background task queue, email provider, observability, backup/restore strategy, retention rules, and deployment topology after scale, security and operational requirements are known.


## Decision 006 — Shared non-MC export schema (14 November 2026)

The user supplied CSV samples for All Complaints (47 columns) and MC (8 columns). The user clarified that every portal download other than MC uses the same 47-column format as `complaints.csv`, including Pending, Vendor Approval, Pending CCI Approval, Master Data 2025/2026 and Batch Export. `apps/core/export_schemas.py` routes all named non-MC sections to the shared 47-column schema and MC to its separate 8-column schema. Helpers are not yet connected to live views or data; row-selection/filter behavior and workbook formatting remain to be implemented/verified.


## v0.2.2 — Work Done reference and execution handover (14 Nov 2026)
- Recorded 47 distinct exact combined `Work Done` values found in the 714-row supplied export sample (625 non-empty rows). This is sample-derived reference data, not a claim that the technician app's complete master list contains only 47 values.
- MC source rows already contain `materialCode` and `materialDescription`; do not require a separate mapping file for the supplied flow or fabricate codes when missing.
- Added Windows PowerShell SQLite quick-start and PostgreSQL Docker instructions. Documented that `.env.example` is not automatically loaded by current settings.
- Scope remains a starter foundation; operational complaint workflows and database-backed exports are not yet implemented.


## v0.2.2 — Work Done reference and execution handover (14 Nov 2026)
- Recorded 47 distinct exact combined `Work Done` values found in the 714-row supplied export sample (625 non-empty rows). This is sample-derived reference data, not a claim that the technician app's complete master list contains only 47 values.
- MC source rows already contain `materialCode` and `materialDescription`; do not require a separate mapping file for the supplied flow or fabricate codes when missing.
- Added Windows PowerShell SQLite quick-start and PostgreSQL Docker instructions. Documented that `.env.example` is not automatically loaded by current settings.
- Scope remains a starter foundation; operational complaint workflows and database-backed exports are not yet implemented.
