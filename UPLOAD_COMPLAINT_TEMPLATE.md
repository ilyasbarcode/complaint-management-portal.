# Upload Complaint Excel Input — Confirmed Format

**Source:** user-provided screenshot, confirmed by the user on 15 November 2026.

The Upload Complaint input contains exactly these 13 columns, in this order:

1. `S.No`
2. `CRMID`
3. `Notification No`
4. `Order No`
5. `Equipment No`
6. `Distributor`
7. `Customer Name`
8. `Phone No`
9. `Address`
10. `City Name`
11. `Remarks`
12. `Territory`
13. `Ref. Type`

A blank Excel template is included as `templates/Upload_Complaint_Template.xlsx`.

The code provides a header validator and row reader for the first worksheet. It rejects a workbook whose first-row headers differ in spelling or order. It skips fully blank rows. It does not yet save records to a database or implement the portal's actual upload action. Required/optional fields, duplicate handling, accepted file size, sheet-name requirements, data type constraints, and post-upload status behavior have not been confirmed, so no such rules are assumed.
