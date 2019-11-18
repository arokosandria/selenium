import unittest
from unittest import TestCase
from selenium import webdriver


class PythonOrgTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

    def tearDown(self) -> None:
        self.driver.close()


    def test_radio_single(self):
        input_field_male= self.driver.find_element_by_css_selector('.panel-body > .radio-inline:nth-child(2) > input')
        input_field_female = self.driver.find_element_by_css_selector('.panel-body > .radio-inline:nth-child(3) > input')
        button= self.driver.find_element_by_xpath('//*[@id="buttoncheck"]')
        input_field_male.click()
        assert  input_field_male.is_selected()
        button.click()
        assert "Radio button 'Male' is checked" in self.driver.page_source

    def test_radio_double(self):
        input_field_male = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label[1]')
        input_field_male.click()
        input_field_age = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input')
        input_field_age.click()
        button= self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/button')
        button.click()
        assert 'Sex : Male' in self.driver.page_source
        assert 'Age group: 15 - 50' in self.driver.page_source


if __name__ == '__main__':
     unittest.main()

