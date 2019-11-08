from appium import webdriver


class Driver:
    def __init__(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Pixel XL API 25 2'
        desired_caps['appPackage'] = 'com.example.android.apis'
        desired_caps['appActivity'] = 'com.example.android.apis.ApiDemos'

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
