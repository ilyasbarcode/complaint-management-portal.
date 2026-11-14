# Complaint Management Portal — Requirements Specification
Version 1.0 | 15 November 2026

## 1. Objective
Build an independent, professional, responsive, multi-user complaint management portal based on workflows and file formats shared by the user. Existing portal is observed only through authorized normal-user access; do not bypass access controls or copy private production data.

## 2. Confirmed modules and requirements
### 2.1 Login and access
- Secure login is required.
- Multi-user and role-based access are desired.
- Exact roles, permissions, password/reset policy and account provisioning remain to be confirmed.

### 2.2 Dashboard
- Dashboard landing page with live counts and analytics.
- Previously observed cards/charts included All Complaints, Unassigned, Assigned, Resolved Breakdown, Feedback Statuses, Customer Feedback, Most Used Materials, Top Distributors and Resolved Level.
- Historical numbers seen in recordings are snapshots only and must not be hardcode as live data.

### 2.3 Upload Complaint
Confirmed input workbook has exactly 13 columns, in this order:
`S.No, CRMID, Notification No, Order No, Equipment No, Distributor, Customer Name, Phone No, Address, City Name, Remarks, Territory, Ref. Type`.
- Validate workbook headers and read rows.
- User-facing import, transaction, duplicate handling, required fields and update/skip policy are pending confirmation.

### 2.4 All Complaints
- Shared non-MC export schema has exactly 47 columns (see `apps/core/export_schemas.py`).
- Previously observed UI included search-by/value, upload date range, distributor, city, advanced filters, card/table views, per-column search, column visibility/reordering, pagination (20/page in recording).
- Complaint details, attachment access, live data filtering, and exact filter semantics remain to be implemented/verified.

### 2.5 Pending CCI Approval
- Complaint details popup includes CRMID, Distributor, Customer Name, Notification No, Contact Number, Ref. Type, Address, Contact Person Name, Tech Shop Name, Resolution Details, Resolve Date, Resolution Time, Resolved By, Issue/Work Done, attachments and parts/material list.
- Feedback modal includes Remarks, `Send back Vendor`, and `Approved`.
- CCI approval is the gate before MC generation.
- Exact status names/transitions, permission rules, re-submission behavior and audit requirements remain to be confirmed.

### 2.6 Technician remarks and material selection
- `Issue` and `Work Done` are standardized remarks integrated from the technician application, not arbitrary free text.
- Technicians select parts/actions in their application; selected parts/actions are incorporated into Work Done.
- The screenshots show two columns: `Issue` and `Work Done`, with many combinations.
- The supplied complaints export contains 47 distinct non-empty Work Done strings. This is a sample-derived set, not a guarantee of the complete technician-app master.
- The future technician-app closing-process video is needed to verify the exact source selection and quantity/warranty rules.
- Do not treat every word in Issue as a material. Use Work Done and verified material aliases; use Issue as context only.

### 2.7 Material Consumption (MC)
- MC is generated only after CCI approval.
- For each approved complaint/order, interpret Work Done to identify selected parts/materials.
- Match each selected material against the authoritative Material Master to obtain exact `materialCode` and `materialDescription`.
- Each material is a separate line item; the same Order No repeats for multiple materials.
- Exact output schema/order:
`CRMID, Notification, Order No, materialCode, materialDescription, Qty, Warranty, Resolve date`.
- User-supplied MC sample has 356 rows and 8 columns. Preserve this structure.
- Filters observed: reporting year (2025/2026), Start Date, End Date, optional Territory, optional Order Numbers; Reset and Generate & Download.
- Do not invent missing material codes, quantities, warranty values or mappings. Unmatched/ambiguous selections must be flagged for review.
- The material master was shown in an image but a verified machine-readable full list is still required before automatic production mapping.

### 2.8 Export
- Batch export accepts Order Numbers, Notification Numbers and CRM IDs; delimiters include comma, space and newline.
- All non-MC downloads use the same 47-column export schema: All Complaints, Pending, Vendor Approval, Pending CCI Approval, Master Data 2025, Master Data 2026 and Batch Export.
- Exact filtering and authorization rules remain to be implemented.

### 2.9 Master Data
- Master Data 2025 and Master Data 2026 are navigation sections.
- Their downloads use the shared 47-column schema per user clarification.
- Actual edit/import workflows remain unverified.

## 3. Confirmed schemas
- Upload Complaint: 13 columns.
- Non-MC exports: 47 columns.
- MC export: 8 columns.
See `apps/core/upload_schema.py` and `apps/core/export_schemas.py`.

## 4. Non-functional requirements
- Professional responsive interface.
- PostgreSQL production database; SQLite may be used only for local preview/tests.
- Secure authentication, role-based authorization, CSRF protection, validation, audit logs and safe attachment handling.
- Never commit secrets, production customer records, phone numbers, addresses or attachment URLs to GitHub.
- Excel outputs must preserve exact headers and column order.
- Time zone: Asia/Karachi unless explicitly changed.

## 5. Open decisions / required inputs
1. Duplicate CRMID/Order policy during upload: reject, skip or update?
2. Required fields and validation rules for 13-column upload.
3. Exact CCI status transitions and who may approve/send back.
4. Full machine-readable Material Master List with exact codes/descriptions and aliases used in Work Done.
5. Qty and Warranty derivation: technician-app data, material defaults, or another rule?
6. Technician-app video showing part selection and complaint closing.
7. User roles and permissions.
8. Attachment storage/retention and access rules.
9. Confirm whether the technician app sends material IDs/quantities directly or only composed remarks.

## 6. Acceptance criteria
- Upload accepts only the confirmed 13-column template and reports invalid headers clearly.
- Complaint records persist only after agreed duplicate/validation rules are configured.
- Only CCI-approved complaints can enter MC generation.
- MC rows match selected materials to exact master codes and follow the 8-column schema.
- Unmatched or ambiguous materials block/flag MC rather than silently inventing data.
- Every non-MC export has exactly the shared 47-column schema.
- Approval actions are permission-controlled and auditable.
- Automated tests cover schema validation, approval gate, material matching, duplicate handling (after rule confirmed), and export headers.
