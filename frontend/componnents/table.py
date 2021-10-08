from selenium import webdriver


class Table:
    """
    Komponent tabeli
    #TODO Do stworzenia
    """
    def __init__(self, driver: webdriver, xpath: str):
        """
        Podstawowy element
        :param driver:
        :param xpath:
        """
        self.driver = driver
        self.xpath = xpath

    def scroll(self):
        """
        Przewinięcie do elementu dla elementów z możliwością przewijania
        :return:
        """
        self.driver.location_once_scrolled_into_view()
