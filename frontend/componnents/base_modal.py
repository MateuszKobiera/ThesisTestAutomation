from selenium import webdriver

from frontend.Pages.base_page import BasePage


class BaseModal(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.xpath = '//div[@class = "ReactModalPortal"]'
        self.save_xpath = self.xpath + '//div[@data-testid = "DialogContainer"]/div[2]/div[2]'
        self.cancel_xpath = self.xpath + '//div[@data-testid = "DialogContainer"]/div[2]/div[1]'
        self.wait_for_element(('//div[@class = "ABB_CommonUX_Dialog__content"]', 'Base'))

    def save(self):
        """
        Kliknięcie przycisku 'save' lub 'accept'
        :return:
        """
        self.get_element((self.save_xpath, 'Button')).click()

    def cancel(self):
        """
        Kliknięcie przycisku 'Cancel'
        :return:
        """
        self.get_element((self.cancel_xpath, 'Button')).click()

