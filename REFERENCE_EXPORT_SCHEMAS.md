# Verified Export Schema Notes — v0.2.2

Samples inspected on 14 November 2026. Only headers, structural metadata and the standardized Work Done strings are retained; customer rows, phone numbers, addresses and attachment URLs are excluded.

## Shared non-MC export format

All portal Excel downloads other than MC use the same exact 47-column format as `complaints.csv`. This applies to All Complaints, All Pending / Pending, Vendor Approval, Pending CCI Approval, Master Data 2025, Master Data 2026 and Batch Export. The format is confirmed; individual row-selection/filter behavior and workbook styling are not.

| # | Exact column header |
|---:|---|
| 1 | `S.No` |
| 2 | `CRMID` |
| 3 | `Notification No` |
| 4 | `Order No` |
| 5 | `Upload Date Time` |
| 6 | `Equipment No` |
| 7 | `Distributor` |
| 8 | `Customer Name` |
| 9 | `Phone No` |
| 10 | `Address` |
| 11 | `City Name` |
| 12 | `Remarks` |
| 13 | `Territory` |
| 14 | `Status` |
| 15 | `Assigned Tech` |
| 16 | `Tech Shop Name` |
| 17 | `Ref. Type` |
| 18 | `Assigned Date` |
| 19 | `Issue` |
| 20 | `Work Done` |
| 21 | `Resolved Date` |
| 22 | `Resolved Duration` |
| 23 | `Outlet customer name` |
| 24 | `Outlet Contact No` |
| 25 | `Location` |
| 26 | `Additional Remarks` |
| 27 | `Final Barcode` |
| 28 | `CCI Remarks` |
| 29 | `Vendor Remarks` |
| 30 | `Vendor Feedback Date` |
| 31 | `NCC Feedback` |
| 32 | `NCC Remarks` |
| 33 | `NCC Reason` |
| 34 | `NCC Feedback Count` |
| 35 | `NCC Feedback Date` |
| 36 | `Technician Feedback` |
| 37 | `Outlet Attachment` |
| 38 | `Barcode Picture` |
| 39 | `After Attachment` |
| 40 | `Customer Feedback Picture` |
| 41 | `Compressor Attachment` |
| 42 | `Close Complaint Attachment` |
| 43 | `GasLeak Attachment` |
| 44 | `More other Parts Attachment` |
| 45 | `Other Parts Attachment` |
| 46 | `Service Attachment` |
| 47 | `NCC User` |

## MC export — separate format

MC is backend-generated Material Consumption. The supplied sample contains 356 data rows and 8 columns. Each material/part used on an order is a separate row, so an Order No may repeat. **Use the `materialCode` and `materialDescription` already present in the generated source data; a separate mapping list is not required for the supplied sample.** Do not invent a code if a future source row has a missing code; flag it for review.

| # | Exact column header |
|---:|---|
| 1 | `CRMID` |
| 2 | `Notification` |
| 3 | `Order No` |
| 4 | `materialCode` |
| 5 | `materialDescription` |
| 6 | `Qty` |
| 7 | `Warranty` |
| 8 | `Resolve date` |

## Work Done standard from technician application

The user confirmed that `Work Done` remarks originate from a standard set integrated from the technician application, rather than arbitrary free text. In the supplied 714-row `complaints.csv` sample, 625 rows have a non-empty Work Done value and there are **47 distinct exact combined strings**. These include multi-action combinations and preserve the original capitalization, punctuation, spacing and trailing commas. The exact values are stored in `apps/core/work_done_standards.py` and covered by tests.

Important: these 47 are the distinct values found in this export sample, not proof that the technician application's full master list contains exactly 47 choices. The technician application remains the source of truth; do not silently normalize or rewrite these strings.

## Implementation status

`apps/core/export_schemas.py` defines output schemas and helper functions only. It is not connected to live database queries or portal download views. The Work Done values are recorded as reference data; they are not yet wired into an operational technician integration or complaint workflow.

Still pending: Upload Complaint input workbook and its validations; detailed role/permission matrix; confirmed status transitions; and implementation of complaint CRUD, approvals, live exports, MC generation and master-data workflows.
