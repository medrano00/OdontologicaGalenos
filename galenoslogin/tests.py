from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestGalenos(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_g01(self):
        print("TestG01")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_username").send_keys("fespinoza")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("fabo1234")
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Usuario ha iniciado sesión satisfactoriamente"
        alert.accept()
        time.sleep(1)
        self.selenium.get("http://localhost:8000/galenoslogin/indexwithlogin")
        time.sleep(3)
        self.selenium.find_element(By.ID, "navbardrop").click()
        time.sleep(1)
        self.selenium.find_element(By.LINK_TEXT, "Administrador").click()
        time.sleep(1)
        reservas = self.selenium.find_elements(By.XPATH, "/html/body/table/tbody//tr")
        for reserva in reservas:
            print(reserva.text)
        time.sleep(1)