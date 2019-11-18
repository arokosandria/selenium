import unittest
from unittest import TestCase
from selenium import webdriver


class PythonOrgTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    def tearDown(self) -> None:
        self.driver.close()

    def test_input_form_one(self):
        input_field = self.driver.find_element_by_id('user-message')
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
        input_field.send_keys('Karolina')
        button.click()
        assert 'Karolina' in self.driver.page_source

    def test_input_form_two(self):
        input_field_one= self.driver.find_element_by_id('sum1')
        input_field_two = self.driver.find_element_by_id('sum2')
        input_field_one.send_keys('2')
        input_field_two.send_keys('3')
        button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
        button.click()
        assert '5' in self.driver.page_source

if __name__ == '__main__':
    unittest.main()