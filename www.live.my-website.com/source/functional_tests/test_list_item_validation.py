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
    @skip
    def test_cannot_add_empty_list_items(self):

        #commit a empty todo thing
        #press enter without input

        #the page refreshed and show an error messege
        #the messege shows the todo thing cannot be empty

        #she typed some text and commit, this time it's ok

        #she committed another empty todo-thing once again

        #she saw a similar error messege at list page

        #it's ok after she typed some text
        self.fail('write me')