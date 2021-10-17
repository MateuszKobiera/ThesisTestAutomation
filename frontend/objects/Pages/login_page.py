from selenium import webdriver

from frontend.Locators.Pages.login_locators import LoginPageLocators
from frontend.objects.Pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/auth'
        self.wait_for_element(LoginPageLocators.login_button, timeout=8)

    def set_username(self, username: str) -> None:
        """
        Wpisanie nazwy użytkownika.
        :return:
        """
        self.get_element(LoginPageLocators.username_input).set_value(username)

    def get_username_validation(self) -> None:
        """
        Pobranie walidacji dla nazwy użytkownika
        :return:
        """
        return self.get_element(LoginPageLocators.username_input).get_validation()

    def set_password(self, password: str) -> None:
        """
        Wpisanie hasła dla użytkownika
        :return: tekst walidacji
        """
        self.get_element(LoginPageLocators.password_input).set_value(password)

    def get_password_validation(self) -> None:
        """
        Pobranie walidacji dla hasła użytkownika
        :return: tekst walidacji
        """
        return self.get_element(LoginPageLocators.password_input).get_validation()

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

    def get_general_validation(self) -> str:
        """
        Pobranie ogólnej walidacji
        :return:
        """
        if self.check_is_element_visible(LoginPageLocators.general_validation_base):
            return self.get_element(LoginPageLocators.general_validation_base).get_text()
        else:
            return ''

