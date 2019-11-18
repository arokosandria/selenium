import unittest
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class PythonOrgTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/javascript-alert-box-demo.html')

    def tearDown(self) -> None:
        self.driver.close()

    def test_java_alert(self):
        button= self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/button')
        button.click()
        self.driver.switch_to.alert.accept()

    def test_java_confirm(self):
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/button')
        button.click()
        self.driver.switch_to.alert.dismiss()
        assert 'You pressed Cancel!' in self.driver.page_source
        button.click()
        self.driver.switch_to.alert.accept()
        assert 'You pressed OK!' in self.driver.page_source

    def test_java_alert(self):
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/button')
        button.click()
        self.driver.switch_to.alert.send_keys('Karolina')
        self.driver.switch_to.alert.accept()
        time.sleep(10)
        assert "You have entered 'Karolina' !" in self.driver.page_source
        button.click()
        self.driver.switch_to.alert.dismiss()
        assert "You have entered 'Karolina' !" in self.driver.page_source

if __name__ == '__main__':
     unittest.main()