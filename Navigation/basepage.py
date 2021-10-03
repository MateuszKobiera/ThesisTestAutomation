from selenium.webdriver.common.by import By


def get_element(element_locator):
    return NavBasePage.driver.find_element(By.XPATH, element_locator)



