import unittest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jsonRead import read_json_data
import time

class commonUtil(unittest.TestCase):

    def click(self, element, method):

        if method == 'xpath':
            self.first_click = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((MobileBy.XPATH, read_json_data.json_Reads(self, element))))
            self.driver.instance.find_element(MobileBy.XPATH, read_json_data.json_Reads(self, element)).click()
            time.sleep(1)

        elif method == 'id':
            self.first_click = WebDriverWait(self.driver.instance, 5).until(
                EC.visibility_of_element_located((MobileBy.ID, read_json_data.json_Reads(self, element))))
            self.driver.instance.find_element(MobileBy.ID, read_json_data.json_Reads(self, element)).click()
            time.sleep(1)

    def get_data(self, path):
        WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((MobileBy.CLASS_NAME, path)))
        get = self.driver.instance.find_element_by_class_name(path)
        return get.text

    def IsPresent(self, path):
        try:
            self.driver.instance.find_element(MobileBy.XPATH, read_json_data.json_Reads(self, path))
            return 'true'
        except Exception:
            return 'false'



