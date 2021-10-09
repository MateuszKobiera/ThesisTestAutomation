from selenium import webdriver

from frontend.Locators.terms_condition_locators import TermsAndConditionsLocators
from frontend.Pages.base_page import BasePage


class TermsAndConditionsPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/system/initialization'

    def scroll_terms(self):
        terms_textbox = self.get_element(TermsAndConditionsLocators.terms_condition_textbox)
        terms_textbox.click()
        self.driver.execute_script('arguments[0].scrollIntoView()', terms_textbox)
        self.driver.executeScript('window.scrollTo(0,670);')

