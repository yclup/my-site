from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from unittest import skip
from .base import FunctionalTest
MAX_WAIT = 10




class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):

        #commit a empty todo thing
        #press enter without input
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #the page refreshed and show an error messege
        #the messege shows the todo thing cannot be empty
        error = self.browser.find_element_by_css_selector('.alert-warning')
        self.assertEqual(error.text, "You can't have an empty list item")

        #she typed some text and commit, this time it's ok
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.wait_for_row_in_list_table('1: Buy milk')

        #she committed another empty todo-thing once again
        self.browser.find_element_by_id('id_new_item').send_keys('/n')

        #she saw a similar error messege at list page
        self.wait_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.alert-warning')
        self.assertEqual(error.text, "You can't have an empty list item")

        #it's ok after she typed some text
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
        self.fail('write me')