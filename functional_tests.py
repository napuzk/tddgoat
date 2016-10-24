from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
import os

os.environ["PATH"] += os.pathsep + '/usr/local/bin/'

class NewVisitorTest(unittest.TestCase):
    def setUp(self):

        binary = FirefoxBinary(r'/usr/local/bin/firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.  She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box ( Edith's hobby 
        # is tying fly-fishing lures)
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        
        # There is still a text box inviting her to add another item.  She 
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.  Then she sees
        # that the site has generated a unique URL for her -- There is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satifsfied, she goes back to sleep
        # browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

