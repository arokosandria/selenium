import unittest
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class PythonOrgTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')

    def tearDown(self) -> None:
        self.driver.close()

    def test_list_single(self):
        input_field= Select(self.driver.find_element_by_id('select-demo'))
        input_field.select_by_index(1)
        assert 'Day selected :- Sunday' in self.driver.page_source

    def test_list_multiple(self):
        input_field = Select(self.driver.find_element_by_id('multi-select'))
        input_field.select_by_visible_text("California")
        input_field.select_by_visible_text("Florida")

        button_first=self.driver.find_element_by_xpath('//*[@id="printMe"]')
        button_two=self.driver.find_element_by_xpath('//*[@id="printAll"]')
        button_first.click()
        assert 'First selected option is : Florida' in self.driver.page_source
        button_two.click()
        assert 'Options selected are : Florida' in self.driver.page_source

if __name__ == '__main__':
     unittest.main()