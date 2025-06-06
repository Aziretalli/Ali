import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):
    def setUp(self):
        
        chrome_options = Options()
        
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280x800")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://letsusedata.com/index.html")
        time.sleep(2)

    def test_successful_login(self):
        driver = self.driver
        driver.find_element(By.ID, "txtUser").send_keys("test1")
        driver.find_element(By.ID, "txtPassword").send_keys("Test12456")
        driver.find_element(By.ID, "txtPassword").send_keys(Keys.RETURN)
        time.sleep(2)

        
        self.assertNotIn("index.html", driver.current_url.lower())

    def test_unsuccessful_login(self):
        driver = self.driver
        driver.find_element(By.ID, "txtUser").send_keys("test1")
        driver.find_element(By.ID, "txtPassword").send_keys("test1234")  
        driver.find_element(By.ID, "txtPassword").send_keys(Keys.RETURN)
        time.sleep(2)

        
        self.assertIn("index.html", driver.current_url.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
