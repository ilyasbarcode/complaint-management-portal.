import unittest
import pandas as pd
from apps.core.export_schemas import (
    ALL_COMPLAINTS_EXPORT_COLUMNS, MC_EXPORT_COLUMNS, NON_MC_EXPORT_SECTIONS,
    get_export_columns, select_export_columns,
)


class ExportSchemaTests(unittest.TestCase):
    def test_complaints_schema_has_47_columns(self):
        self.assertEqual(len(ALL_COMPLAINTS_EXPORT_COLUMNS), 47)

    def test_mc_schema_has_8_columns(self):
        self.assertEqual(len(MC_EXPORT_COLUMNS), 8)

    def test_all_non_mc_sections_use_the_same_47_column_schema(self):
        for section in NON_MC_EXPORT_SECTIONS:
            with self.subTest(section=section):
                self.assertEqual(get_export_columns(section), ALL_COMPLAINTS_EXPORT_COLUMNS)
        self.assertEqual(get_export_columns("mc"), MC_EXPORT_COLUMNS)

    def test_schema_order_is_preserved_and_missing_fields_are_blank(self):
        frame = pd.DataFrame({"Order No": [123], "Unexpected": ["omit"]})
        result = select_export_columns(frame, ("CRMID", "Order No"))
        self.assertEqual(list(result.columns), ["CRMID", "Order No"])
        self.assertEqual(result.loc[0, "CRMID"], "")
        self.assertEqual(result.loc[0, "Order No"], 123)


if __name__ == "__main__":
    unittest.main()
