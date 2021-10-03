from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element2(browser: webdriver, element_locator):
    WebDriverWait(browser, 5, 0.1).until(visibility_of_element_located((By.XPATH, element_locator)))