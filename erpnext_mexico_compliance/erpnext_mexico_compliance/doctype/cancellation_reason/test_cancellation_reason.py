# Copyright (c) 2024, TI Sin Problemas and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


class TestCancellationReason(IntegrationTestCase):
	def test_cancellation_reasons_require_a_relationship_only_for_code_01(self):
		reasons = frappe.get_all(
			"Cancellation Reason",
			filters={"code": ("in", ("01", "02", "03", "04"))},
			fields=["code", "requires_relationship"],
		)

		self.assertEqual(
			{reason.code: reason.requires_relationship for reason in reasons},
			{"01": 1, "02": 0, "03": 0, "04": 0},
		)
