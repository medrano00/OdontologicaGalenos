from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class LoginTest(LiveServerTestCase):
def G01(self):
    driver = webdriver.Chrome()
    driver.