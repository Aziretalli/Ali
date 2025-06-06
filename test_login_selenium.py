from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or Firefox, Edge, etc.
        self.driver.get("https://letsusedata.com/login")  # Adjust URL if needed
        time.sleep(2)

    def test_successful_login(self):
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("test1")
        driver.find_element(By.NAME, "password").send_keys("Test12456")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertIn("dashboard", driver.current_url.lower())  # Adjust if dashboard URL changes

    def test_unsuccessful_login(self):
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("test1")
        driver.find_element(By.NAME, "password").send_keys("test1234")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(2)
        error_elements = driver.find_elements(By.CLASS_NAME, "error")  # Adjust if needed
        self.assertTrue(any("invalid" in el.text.lower() for el in error_elements))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()