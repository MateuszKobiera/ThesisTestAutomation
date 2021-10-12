from selenium import webdriver

from frontend.Locators.account_initialization_locators import AccountInitializationLocators
from frontend.Modals.base_modal import BaseModal


class AccountInitializationPage(BaseModal):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/account/activation'
        self.wait_for_element(AccountInitializationLocators.company_input, timeout=20)

    def save(self):
        """
        Zapisanie ustawień
        :return:
        """
        self.get_element(AccountInitializationLocators.save_button).click()

    def cancel(self):
        """
        Anulowanie ustawień
        :return:
        """
        self.get_element(AccountInitializationLocators.cancel_button).click()

    def set_company(self, company: str):
        """
        Ustawienie firmy
        :param company: nazwa firmy
        :return:
        """
        self.get_element(AccountInitializationLocators.company_input).set_value(company)

    def set_first_name(self, first_name: str):
        """
        Ustawienie imienia
        :param first_name: Imię
        :return:
        """
        self.get_element(AccountInitializationLocators.first_name_input).set_value(first_name)

    def set_last_name(self, last_name: str):
        """
        Ustawienie nazwiska
        :param last_name: Nazwisko
        :return:
        """
        self.get_element(AccountInitializationLocators.last_name_input).set_value(last_name)

    def set_initials(self, initials: str):
        """
        Ustawienie inicjałów
        :param initials: Inicjały
        :return:
        """
        self.get_element(AccountInitializationLocators.initials_input).set_value(initials)

    def set_email(self, email: str):
        """
        Ustawienie e-maila
        :param email: E-mail
        :return:
        """
        self.get_element(AccountInitializationLocators.email_input).set_value(email)

    def set_phone(self, phone: str):
        """
        Ustawienie numeru telefonu
        :param phone: Numer telefonu
        :return:
        """
        self.get_element(AccountInitializationLocators.phone_input).set_value(phone)
