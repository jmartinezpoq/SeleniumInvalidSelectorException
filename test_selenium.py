import unittest

from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.close()

    def test_wrong_xpath_find_element(self) -> None:
        self.driver.get("https://google.com/ncr")
        with self.assertRaises(InvalidSelectorException):
            self.driver.find_element(By.XPATH, "//*[contains(@id,'something'").click()

    def test_wrong_xpath_find_element_by_xpath(self) -> None:
        self.driver.get("https://google.com/ncr")
        with self.assertRaises(InvalidSelectorException):
            self.driver.find_element_by_xpath("//*[contains(@id,'something'").click()

    def test_wrong_xpath_wait(self) -> None:
        selector = "//*[contains(@id,'something'"
        with self.assertRaises(InvalidSelectorException):
            condition = EC.invisibility_of_element_located((By.XPATH, selector))
            WebDriverWait(self.driver, 15).until(condition)


if __name__ == "__main__":
    unittest.main()
