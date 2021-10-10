from selenium import webdriver

from frontend.Locators.terms_condition_locators import TermsAndConditionsLocators
from frontend.componnents.base_modal import BaseModal


class TermsAndConditionsPage(BaseModal):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/system/initialization'
        self.wait_for_element(TermsAndConditionsLocators.terms_condition_textbox)

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
        self.wait_for_element(TermsAndConditionsLocators.initialize_button)
        self.get_element(TermsAndConditionsLocators.initialize_button).click()
