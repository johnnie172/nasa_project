import unittest
import mock
import input_utilities
import datetime

class TestInputUtilities(unittest.TestCase):
    def test_get_date_from_user(self):
        with mock.patch('builtins.input', return_value="t"):
            self.assertEqual(input_utilities.get_date_from_user(), datetime.datetime.now().date())
        with mock.patch('builtins.input', return_value="a"):
            self.assertEqual(input_utilities.get_date_from_user(), input_utilities.get_another_date_from_user())

    def test_get_another_date_from_user(self):
        user_input = ["2020", "01", "01"]
        with mock.patch('builtins.input', side_effect=user_input):
            self.assertEqual(input_utilities.get_another_date_from_user(),"2020-01-01")

    def test_get_quality_from_user(self):
        with mock.patch('builtins.input', return_value="hd"):
            self.assertEqual(input_utilities.get_quality_from_user(), ["hdurl"])



