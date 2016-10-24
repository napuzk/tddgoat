from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

os.environ["PATH"] += os.pathsep + '/usr/local/bin/'

binary = FirefoxBinary(r'/usr/local/bin/firefox')

browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
