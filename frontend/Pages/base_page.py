from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.base_url = 'http://localhost:3000/'

    def get_element(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def wait_for_element(self, element_locator):
        WebDriverWait(self.driver, 5, 0.1).until(visibility_of_element_located((By.XPATH, element_locator)))
