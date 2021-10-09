from selenium import webdriver

from frontend.Locators.initialization_locators import InitializationLocators
from frontend.Pages.base_page import BasePage


class InitializationPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/admin/activation'
        self.wait_for_element(InitializationLocators.change_password_button)

    def set_passwords(self, password: str, password_confirmation: str) -> None:
        """
        Ustawienie hasła dla Admina
        :return:
        """
        self.get_element(InitializationLocators.password_input).set_input(password)
        self.get_element(InitializationLocators.password_confirmation_input).set_input(password_confirmation)

    def change_password(self) -> None:
        """
        Kliknięcie przycisku zmiany hasła
        :return:
        """
        self.get_element(InitializationLocators.change_password_button).click()
