from selenium import webdriver

from frontend.Pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.login_url = self.base_url + '#/auth'



