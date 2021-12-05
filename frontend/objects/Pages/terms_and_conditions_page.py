from selenium import webdriver

from frontend.locators.Pages.terms_condition_locators import TermsAndConditionsLocators
from frontend.objects.Pages.base_page import BasePage


class TermsAndConditionsPage(BasePage):

    def __init__(self, driver: webdriver, wait: bool = True) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/system/initialization'
        if wait:
            self.get_element(TermsAndConditionsLocators.terms_condition_textbox).wait_for_element()

    def save(self):
        """
        Kliknięcie przycisku 'save' lub 'accept'
        :return:
        """
        self.get_element(TermsAndConditionsLocators.save_button).click()

    def cancel(self):
        """
        Kliknięcie przycisku 'Cancel'
        :return:
        """
        self.get_element(TermsAndConditionsLocators.cancel_button).click()

    def scroll_terms_and_policy(self):
        """
        Zejście na dół Terms&Conditions i Privacy policy
        :return:
        """
        terms_textbox = self.get_element(TermsAndConditionsLocators.terms_condition_textbox)
        terms_textbox.click()
        self.driver.execute_script('var terms = document.getElementById("terms-and-conditions-textbox");'
                                   'terms.scrollTop = terms.scrollHeight;')
        self.driver.execute_script('var privacy = document.getElementById("privacy-policy-textbox");'
                                   'privacy.scrollTop = privacy.scrollHeight;')

    def accept_terms_and_policy(self):
        """
        Kliknięcie checkboxu aby zaakceptować Terms & Conditions
        :return:
        """
        terms_condition_checkbox = self.get_element(TermsAndConditionsLocators.terms_condition_checkbox)
        if terms_condition_checkbox.driver.is_enabled():
            terms_condition_checkbox.click()
        privacy_policy_checkbox = self.get_element(TermsAndConditionsLocators.privacy_policy_checkbox)
        if privacy_policy_checkbox.driver.is_enabled():
            privacy_policy_checkbox.click()

    def launch_initialization(self):
        """
        Potwierdzenie inicjacji użytkownika
        :return:
        """
        element = self.get_element(TermsAndConditionsLocators.initialize_button)
        element.wait_for_element()
        element.click()
