from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

# Added to support new geckodriver thing
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import unittest
import sys

# Added to support new geckodriver thing
import os
# Define path to firefox and geckodriver
os.environ["PATH"] += os.pathsep + '/usr/local/bin/'

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        # Define location of firefox binary for geckodriver
        binary = FirefoxBinary(r'/usr/local/bin/firefox')
        # Pass location of firefox binary to the webdriver
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
