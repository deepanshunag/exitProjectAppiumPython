import unittest
from driver_file import Driver
import time
from common_util import commonUtil
import pytest

'''
to run 
pytest -v -s --html=report2.html --self-contained-html test_runner.py
'''
class test_runner(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    @pytest.mark.first
    def test_second_task(self):
        commonUtil.click(self, 'App', 'xpath')
        commonUtil.click(self, 'ActionBar', 'id')
        commonUtil.click(self, 'DisplayOptions', 'xpath')
        check = commonUtil.get_data(self, 'android.widget.TextView')
        commonUtil.click(self, 'DisplayShowTitle', 'id')
        check1 = commonUtil.get_data(self, 'android.widget.TextView')
        self.assertNotEqual(check,check1)
        commonUtil.click(self, 'DisplayShowTitle', 'id')
        check2 = commonUtil.get_data(self, 'android.widget.TextView')
        self.assertEqual(check,check2)
        time.sleep(3)

    @pytest.mark.second
    def test_first_task(self):
        commonUtil.click(self, 'animation', 'xpath')
        commonUtil.click(self, 'Hide-Show Animations', 'xpath')
        commonUtil.click(self, 'Button0', 'xpath')
        commonUtil.click(self, 'Button1', 'xpath')
        commonUtil.click(self, 'Button2', 'xpath')
        commonUtil.click(self, 'Button3', 'xpath')
        check_true = commonUtil.IsPresent(self, 'Button3')
        self.assertEqual(check_true, 'false')
        commonUtil.click(self, 'AddNewButton', 'id')
        check_true = commonUtil.IsPresent(self, 'Button3')
        self.assertEqual(check_true, 'true')

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_runner)
    unittest.TextTestRunner(verbosity=2).run(suite)