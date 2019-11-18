import unittest
from unittest import TestCase
from selenium import webdriver


class PythonOrgTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

    def tearDown(self) -> None:
        self.driver.close()

    def test_checkbox_single(self):
        input_field = self.driver.find_element_by_id('isAgeSelected')
        input_field.click()
        assert 'Success - Check box is checked' in self.driver.page_source

    def test_checkbox_multiple(self):
        button = self.driver.find_element_by_id('check1')
        button.click()
        assert 'Uncheck All' in self.driver.page_source
        input_field_one = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label/input')
        input_field_two = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label/input')
        input_field_three = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/label/input')
        input_field_four = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[4]/label/input')
        assert input_field_one.is_selected()
        assert input_field_two.is_selected()
        assert input_field_three.is_selected()
        assert input_field_four.is_selected()
        input_field_one.click()
        self.assertFalse(input_field_one.is_selected())
        assert 'Check All' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()
