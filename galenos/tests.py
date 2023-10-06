from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.

class HostTest(LiveServerTestCase):
    def testhomepage(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/index/')
        assert "Odontológica Galenos" in driver.title