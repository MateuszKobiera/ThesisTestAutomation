from selenium import webdriver

from frontend.objects.Pages.base_page import BasePage


class BaseModal(BasePage):
    """
    Podstawowe okno dialogowe
    """
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.xpath = '//div[@class = "ReactModalPortal"]'
        self.save_xpath = \
            f'({self.xpath}//div[@data-testid = "DialogContainer"]//button[contains(@class, "primaryblue")])[last()]'
        self.cancel_xpath = \
            f'({self.xpath}//div[@data-testid = "DialogContainer"]//button[contains(@class, "discreetblack")])[last()]'
        self.x_close_button = "//div[@class='ReactModalPortal']//i[contains(@class, 'close_24')]"
        self.title = "//span[contains(@class, 'title')]"
        self.wait_for_element(('//div[@class = "ABB_CommonUX_Dialog__content"]', 'Base'))

    def save(self) -> None:
        """
        Kliknięcie przycisku 'save' lub 'accept'
        :return:
        """
        save_button = (self.save_xpath, 'Button')
        self.get_element(save_button).click()
        self.wait_for_element_to_disappear(save_button, timeout=10)

    def cancel(self) -> None:
        """
        Kliknięcie przycisku 'Cancel'
        :return:
        """
        self.get_element((self.cancel_xpath, 'Button')).click()

    def close(self) -> None:
        """
        Kliknięcie przycisku 'X' jako zamknięcie okna dialogowego i anulowanie operacji
        :return:
        """
        self.get_element((self.x_close_button, 'Button')).click()

    def get_title(self) -> str:
        """
        Pobranie tytułu okna dialogowego
        :return: tekst tytułu
        """
        return self.get_element((self.title, 'Base')).get_text()
