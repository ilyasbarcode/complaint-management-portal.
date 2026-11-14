import unittest
from apps.core.mc_workflow import (
    MCWorkflowError, MaterialRule, build_mc_rows, is_cci_approved,
    select_materials_from_work_done,
)

class MCWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.rule = MaterialRule(
            material_code="660-002-083",
            material_description="FAN MOTOR 10W",
            aliases=("FAN MOTOR 10W REPLACED",),
            default_qty="1",
            warranty="In Warranty",
        )

    def test_only_approved_status_is_eligible(self):
        self.assertTrue(is_cci_approved("Approved"))
        self.assertFalse(is_cci_approved("Pending CCI Approval"))

    def test_material_alias_is_matched_from_work_done(self):
        selected = select_materials_from_work_done(
            "FAN MOTOR 10W REPLACED,Condenser Service,", [self.rule]
        )
        self.assertEqual([x.material_code for x in selected], ["660-002-083"])

    def test_unmatched_material_is_flagged(self):
        complaint = {"Status":"Approved", "Work Done":"Condenser Service,"}
        with self.assertRaises(MCWorkflowError):
            build_mc_rows(complaint, [self.rule])

    def test_pending_complaint_cannot_generate_mc(self):
        complaint = {"Status":"Pending CCI Approval", "Work Done":"FAN MOTOR 10W REPLACED,"}
        with self.assertRaises(MCWorkflowError):
            build_mc_rows(complaint, [self.rule])

    def test_mc_output_has_exact_eight_columns(self):
        complaint = {"Status":"Approved", "CRMID":"C1", "Notification No":"N1",
                     "Order No":"O1", "Work Done":"FAN MOTOR 10W REPLACED,",
                     "Resolved Date":"2026-11-14"}
        row = build_mc_rows(complaint, [self.rule])[0]
        self.assertEqual(list(row), ["CRMID", "Notification", "Order No", "materialCode",
                                     "materialDescription", "Qty", "Warranty", "Resolve date"])
        self.assertEqual(row["Order No"], "O1")

if __name__ == "__main__":
    unittest.main()
