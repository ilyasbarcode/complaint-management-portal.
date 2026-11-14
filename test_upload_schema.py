import tempfile
import unittest
from pathlib import Path
from openpyxl import Workbook
from apps.core.upload_schema import (
    UPLOAD_COMPLAINT_COLUMNS,
    create_upload_complaint_template,
    validate_upload_complaint_workbook,
)


class UploadComplaintSchemaTests(unittest.TestCase):
    def test_template_uses_exact_13_headers(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "upload_template.xlsx"
            create_upload_complaint_template(path)
            wb = Workbook()
            wb = __import__('openpyxl').load_workbook(path, read_only=True)
            self.assertEqual(tuple(c.value for c in next(wb.active.iter_rows())), UPLOAD_COMPLAINT_COLUMNS)
            wb.close()

    def test_valid_workbook_rows_are_returned(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "valid.xlsx"
            wb = Workbook(); ws = wb.active
            ws.append(list(UPLOAD_COMPLAINT_COLUMNS))
            ws.append([1, "CRM-1", "N-1", "O-1", "EQ-1", "Distributor", "Customer", "0300", "Address", "City", "Remark", "Territory", "R134"])
            wb.save(path)
            rows = validate_upload_complaint_workbook(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["CRMID"], "CRM-1")

    def test_wrong_header_order_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "wrong.xlsx"
            wb = Workbook(); wb.active.append(list(reversed(UPLOAD_COMPLAINT_COLUMNS))); wb.save(path)
            with self.assertRaises(ValueError):
                validate_upload_complaint_workbook(path)


if __name__ == "__main__":
    unittest.main()
