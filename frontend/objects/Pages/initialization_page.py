from selenium import webdriver

from frontend.locators.Pages.initialization_locators import InitializationLocators
from frontend.objects.Pages.base_page import BasePage


class InitializationPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/admin/activation'
        self.get_element(InitializationLocators.change_password_button).wait_for_element()
        self.title = 'Building Ecosystem'

    @property
    def password_input(self):
        return self.get_element(InitializationLocators.password_input)

    @property
    def password_confirmation_input(self):
        return self.get_element(InitializationLocators.password_confirmation_input)

    def set_passwords(self, password: str, password_confirmation: str) -> None:
        """
        Ustawienie hasła dla Admina
        :return:
        """
        self.get_element(InitializationLocators.password_input).set_value(password)
        self.get_element(InitializationLocators.password_confirmation_input).set_value(password_confirmation)

    def change_password(self) -> None:
        """
        Kliknięcie przycisku zmiany hasła
        :return:
        """
        self.get_element(InitializationLocators.change_password_button).click()

    def get_first_password_validation(self) -> str:
        """
        Pobranie walidacji dla pierwszego pola do wpisania danych hasła
        :return: tekst walidacji
        """
        return self.get_element(InitializationLocators.password_input).get_validation()

    def get_confirm_password_validation(self) -> str:
        """
        Pobranie walidacji dla pola do potwierdzenia wpisania hasła
        :return: tekst walidacji
        """
        return self.get_element(InitializationLocators.password_confirmation_input).get_validation()

    def get_title(self) -> str:
        """
        Pobranie tytułu strony
        :return: tekst tytuły
        """
        return self.get_element(InitializationLocators.title_base).get_text()
