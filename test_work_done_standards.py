import unittest
from apps.core.work_done_standards import WORK_DONE_STANDARD_VALUES, is_sample_standard_work_done


class WorkDoneStandardTests(unittest.TestCase):
    def test_sample_contains_47_distinct_combined_values(self):
        self.assertEqual(len(WORK_DONE_STANDARD_VALUES), 47)
        self.assertEqual(len(set(WORK_DONE_STANDARD_VALUES)), 47)

    def test_exact_original_format_is_preserved(self):
        self.assertTrue(is_sample_standard_work_done("Condenser Service,"))
        self.assertTrue(is_sample_standard_work_done("Gas Charged,Condenser Service,"))
        self.assertFalse(is_sample_standard_work_done("condenser service"))


if __name__ == "__main__":
    unittest.main()
