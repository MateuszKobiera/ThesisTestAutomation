from copy import copy

from selenium import webdriver

from frontend.elements.base_element import BaseElement


class Table:
    """
    Komponent tabeli
    """

    def __init__(self, driver: webdriver, xpath: str):
        """
        Podstawowy element
        :param driver:
        :param xpath:
        """
        self.driver = driver
        self.xpath = xpath

    def get_element(self, locator_xpath: str) -> webdriver:
        return BaseElement(self.driver.find_element_by_xpath(locator_xpath), locator_xpath)

    def get_head_elements(self) -> list:
        """
        Wybranie elementów nagłówka tabeli
        :return: lista elementów nagłówka
        """
        return self.driver.find_elements_by_xpath(self.xpath + '/thead/tr/th')

    def get_all_rows(self) -> list:
        """
        Wybranie wszystkich rzędu
        :return: lista rzędów
        """
        return self.driver.find_elements_by_xpath(self.xpath + '/tbody/tr')

    def get_row_elements(self, row_id: int) -> list:
        """
        Wybranie rzędu
        :param row_id: numer rzędu (liczone od 1)
        :return: lista elementów rzędu
        """
        return self.driver.find_elements_by_xpath(self.xpath + f'/tbody/tr[{row_id}]/td')

    def get_table(self, unique_column_name: str = None) -> dict:
        """
        Pobranie tabeli jako słownika z wartościami tekstowymi tabeli
        :param unique_column_name: opcjonalny parametr, nazwa kolumny dla której są unikalne wartości rzędów,
        które będą kluczami słownika
        :return:
        """
        table_heads = []
        for element in self.get_head_elements():
            table_heads.append(element.text)
        table_row = {}
        table = {}
        column_index = 0
        for row_id in range(0, len(self.get_all_rows())):
            for element in self.get_row_elements(row_id+1):
                table_row[table_heads[column_index]] = element.text
                column_index += 1
            column_index = 0
            row_name = table_row[unique_column_name] if unique_column_name else row_id
            table[row_name] = copy(table_row)
        return table

    def delete_row(self, row_id: int = None, row_name: str = None) -> webdriver:
        """
        Usunięcie wiersza
        :param row_id: numer wiersza, parametr opcjonalny
        :param row_name: unikalna nazwa wiersza, parametr opcjonalny
        :return: modal z potwierdzeniem usunięcia
        """
        if not row_id and not row_name:
            raise NameError('Należy wybrać, który wiersz usunąć poprzez parametr row_id lub row_name')
        if row_name:
            for row in self.get_table():
                if row_name in row.values():
                    row_id = row
        delete_button = self.xpath + f'/tbody/tr[{row_id}]/td//i[contains(@class,"close")]'
        self.get_element(delete_button).click()
        return self.driver

    def duplicate_row(self, row_id: int = None, row_name: str = None, confirmation: bool = False) -> (webdriver, None):
        """
        Duplikowanie wiersza
        :param row_id: numer wiersza, parametr opcjonalny
        :param row_name: unikalna nazwa wiersza, parametr opcjonalny
        :param confirmation: czy po duplikowanie konieczne jest potwierdzenie?, parametr opcjonalny
        :return: nic jeśli potwierdzenie nie jest wymagane,
        modal z potwierdzeniem duplikowania jeśli potwierdzenie jest konieczne
        """
        if not row_id and not row_name:
            raise NameError('Należy wybrać, który wiersz usunąć poprzez parametr row_id lub row_name')
        if row_name:
            for row in self.get_table():
                if row_name in row.values():
                    row_id = row
        duplicate_button = self.xpath + f'/tbody/tr[{row_id}]/td//i[contains(@class,"copy")]'
        self.get_element(duplicate_button).click()
        if confirmation is True:
            return self.driver
        else:
            return None


    # def scroll(self):
    #     """
    #     Przewinięcie do elementu dla elementów z możliwością przewijania
    #     :return:
    #     """
    #     self.driver.location_once_scrolled_into_view()
