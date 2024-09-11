import unittest
from data_planning import universal_category_list, other_categories, YES, NO, location_of_item
import Planning
from Planning import Planning
class TestPlanningFunctions(unittest.TestCase):

    def test_check_permission_valid(self):
        univ_cat = Planning("2u6")
        result = univ_cat.check_permission()
        self.assertEqual(result, "Permission Required For Site Category: 2U6")

    def test_check_permission_invalid(self):
        with self.assertRaises(Exception) as context:
            Planning("random").check_permission()
        self.assertTrue("Site RANDOM Not In This Category" in str(context.exception))

    def test_check_specific_permission_valid_position(self):
        item_position_yes = YES
        result = Planning("2a6", 1.5, item_position_yes).check_sepcific_permission()
        self.assertEqual(result, "Permission Required For Site Category: 2A6")

    def test_check_specific_permission_invalid_position_height(self):
        item_position_no = NO
        result = Planning("2a6", 1.0, item_position_no).check_sepcific_permission()
        self.assertEqual(result, "Permission Might not be required For Site Category: 2A6")

    def test_check_specific_permission_height_above_2(self):
        item_position_no = NO
        result = Planning("2a6", 2.5, item_position_no).check_sepcific_permission()
        self.assertEqual(result, "Permission Required For Site Category: 2A6")

    def test_check_specific_permission_invalid_category(self):
        with self.assertRaises(Exception) as context:
            Planning("random", 1.5, YES).check_sepcific_permission()
        self.assertTrue("Site RANDOM Not In This Category" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
