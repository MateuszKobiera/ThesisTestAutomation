from selenium import webdriver

from frontend.Locators.login_locators import LoginPageLocators
from frontend.Pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/auth'
        self.wait_for_element(LoginPageLocators.login_button)

    def set_username(self, username: str) -> None:
        """
        Wpisanie nazwy użytkownika.
        :return:
        """
        self.get_element(LoginPageLocators.username_input).set_value(username)

    def set_password(self, password: str) -> None:
        """
        Wpisanie hasła dla użytkownika
        :return:
        """
        self.get_element(LoginPageLocators.password_input).set_value(password)

    def login(self) -> None:
        """
        Kliknięcie przycisku zaloguj
        :return:
        """
        self.get_element(LoginPageLocators.login_button).click()

    def choose_mode(self, mode: str) -> None:
        """
        Wybranie modułu
        :return:
        """
        if mode not in ['Operation', 'Configuration']:
            self.get_element(LoginPageLocators.tool_dropdown).choose_option(mode)
        else:
            ValueError('Zła nazwa modułu. Do wybrania: "Configuration" albo "Operation"')

