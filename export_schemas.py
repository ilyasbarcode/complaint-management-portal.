"""Verified column schemas from user-provided portal export samples.

This module defines column order only. It does not fetch portal records or implement
unverified export workflows. Sample customer data is intentionally not included.
"""

ALL_COMPLAINTS_EXPORT_COLUMNS = (
    'S.No',
    'CRMID',
    'Notification No',
    'Order No',
    'Upload Date Time',
    'Equipment No',
    'Distributor',
    'Customer Name',
    'Phone No',
    'Address',
    'City Name',
    'Remarks',
    'Territory',
    'Status',
    'Assigned Tech',
    'Tech Shop Name',
    'Ref. Type',
    'Assigned Date',
    'Issue',
    'Work Done',
    'Resolved Date',
    'Resolved Duration',
    'Outlet customer name',
    'Outlet Contact No',
    'Location',
    'Additional Remarks',
    'Final Barcode',
    'CCI Remarks',
    'Vendor Remarks',
    'Vendor Feedback Date',
    'NCC Feedback',
    'NCC Remarks',
    'NCC Reason',
    'NCC Feedback Count',
    'NCC Feedback Date',
    'Technician Feedback',
    'Outlet Attachment',
    'Barcode Picture',
    'After Attachment',
    'Customer Feedback Picture',
    'Compressor Attachment',
    'Close Complaint Attachment',
    'GasLeak Attachment',
    'More other Parts Attachment',
    'Other Parts Attachment',
    'Service Attachment',
    'NCC User',
)

# User-confirmed rule (14 November 2026): every Excel download other than MC
# uses the same 47-column layout supplied in complaints.csv, regardless of section.
NON_MC_EXPORT_SECTIONS = (
    "all_complaints", "all_pending", "vendor_approval",
    "pending_cci_approval", "master_data_2025", "master_data_2026", "batch_export",
)


def get_export_columns(section):
    """Return the confirmed output columns for a portal download section."""
    key = str(section).strip().lower()
    if key == "mc":
        return MC_EXPORT_COLUMNS
    if key in NON_MC_EXPORT_SECTIONS:
        return ALL_COMPLAINTS_EXPORT_COLUMNS
    raise ValueError(f"Unknown export section: {section!r}")


MC_EXPORT_COLUMNS = (
    'CRMID',
    'Notification',
    'Order No',
    'materialCode',
    'materialDescription',
    'Qty',
    'Warranty',
    'Resolve date',
)


def select_export_columns(dataframe, columns):
    """Return a copy with exactly the requested columns in the specified order.

    Missing schema columns are added as blank values; extra source columns are
    excluded. The caller remains responsible for authorization and data filtering.
    """
    result = dataframe.copy()
    for column in columns:
        if column not in result.columns:
            result[column] = ""
    return result.loc[:, list(columns)]


def write_export_xlsx(dataframe, columns, output, sheet_name="Export"):
    """Write a DataFrame as an XLSX sheet with an exact, ordered column schema.

    This helper is not wired to a portal view yet; filters, permissions, and source
    queries must be confirmed before connecting it to a download button.
    """
    ordered = select_export_columns(dataframe, columns)
    ordered.to_excel(output, index=False, sheet_name=sheet_name, engine="openpyxl")
    return ordered
