from selenium import webdriver

from frontend.Locators.Pages.my_property_locators import MyPropertyLocators
from frontend.objects.Modals.my_property_add_to_structure import AddToStructureModal
from frontend.objects.Pages.base_page import BasePage
from frontend.components.table import Table


class MyPropertyPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        """
        :param driver:
        """
        super().__init__(driver)
        self.url = self.base_url + '#/app/mysite'
        self.wait_for_element(MyPropertyLocators.property_name_input)

    def set_property_name(self, property_name: str) -> None:
        """
        Ustawienie nazwy nieruchomości
        :param property_name: Nazwa nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.property_name_input).set_value(property_name)

    def get_property_name(self) -> str:
        """
        Pobranie nazwy nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.property_name_input).get_value()

    def get_property_name_validation(self) -> str:
        """
        Pobranie tekstu walidacji nazwy nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.property_name_input).get_validation()

    def set_address(self, address: str) -> None:
        """
        Ustawienie adresu nieruchomości
        :param address: Adres nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.address_input).set_value(address)

    def get_address(self) -> str:
        """
        Pobranie adresu nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.address_input).get_value()

    def get_address_validation(self) -> str:
        """
        Pobranie tekstu walidacji adresu nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.address_input).get_validation()

    def set_zip_code(self, zip_code: str) -> None:
        """
        Ustawienie kodu pocztowego nieruchomości
        :param zip_code: Kod pocztowy nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.zip_code_input).set_value(zip_code)

    def get_zip_code(self) -> str:
        """
        Pobranie kodu pocztowego nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.zip_code_input).get_value()

    def get_zip_code_validation(self) -> str:
        """
        Pobranie tekstu walidacji kodu pocztowego nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.zip_code_input).get_validation()

    def set_town(self, town: str) -> None:
        """
        Ustawienie miasta nieruchomości
        :param town: Miasto nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.town_input).set_value(town)

    def get_town(self) -> str:
        """
        Pobranie miasta nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.town_input).get_value()

    def get_town_validation(self) -> str:
        """
        Pobranie tekstu walidacji miasta nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.town_input).get_validation()
    
    def set_people(self, people: str) -> None:
        """
        Ustawienie liczby ludzi w nieruchomości
        :param people: Liczba ludzi w  nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.people_input).set_value(people)

    def get_people(self) -> str:
        """
        Pobranie liczby ludzi w nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.people_input).get_value()

    def get_people_validation(self) -> str:
        """
        Pobranie tekstu walidacji liczby ludzi w nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.people_input).get_validation()
    
    def set_gross_surface(self, gross_surface: str) -> None:
        """
        Ustawienie powierzchni brutto nieruchomości
        :param gross_surface: Powierzchnia brutto nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.gross_surface_input).set_value(gross_surface)

    def get_gross_surface(self) -> str:
        """
        Pobranie powierzchni brutto nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gross_surface_input).get_value()

    def get_gross_surface_validation(self) -> str:
        """
        Pobranie tekstu walidacji powierzchni brutto nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gross_surface_input).get_validation()
    
    def set_gps_latitude(self, gps_latitude: str) -> None:
        """
        Ustawienie szerokości geograficznej nieruchomości
        :param gps_latitude: Szerokość geograficzna nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.gps_latitude_input).set_value(gps_latitude)

    def get_gps_latitude(self) -> str:
        """
        Pobranie szerokości geograficznej nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gps_latitude_input).get_value()

    def get_gps_latitude_validation(self) -> str:
        """
        Pobranie tekstu walidacji szerokości geograficznej nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gps_latitude_input).get_validation()
    
    def set_gps_longitude(self, gps_longitude: str) -> None:
        """
        Ustawienie długości geograficznej nieruchomości
        :param gps_longitude: Długość geograficzna nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.gps_longitude_input).set_value(gps_longitude)

    def get_gps_longitude(self) -> str:
        """
        Pobranie długości geograficznej nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gps_longitude_input).get_value()

    def get_gps_longitude_validation(self) -> str:
        """
        Pobranie tekstu walidacji długości geograficznej nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.gps_longitude_input).get_validation()
    
    def set_country(self, country: str) -> None:
        """
        Ustawienie kraju nieruchomości
        :param country: Kraj nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.country_dropdown).choose_option(country)

    def get_country(self) -> str:
        """
        Pobranie kraju nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.country_dropdown).get_value()

    def get_country_validation(self) -> str:
        """
        Pobranie tekstu walidacji kraju nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.country_dropdown).get_validation()

    def set_property_type(self, property_type: str) -> None:
        """
        Ustawienie typu nieruchomości
        :param property_type: Typ nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.property_type_dropdown).choose_option(property_type)

    def get_property_type(self) -> str:
        """
        Pobranie typu nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.property_type_dropdown).get_value()

    def get_property_type_validation(self) -> str:
        """
        Pobranie tekstu walidacji typu nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.property_type_dropdown).get_validation()
    
    def set_main_usage(self, main_usage: str) -> None:
        """
        Ustawienie głównej użyteczności nieruchomości
        :param main_usage: Główna użyteczność nieruchomości
        :return:
        """
        self.get_element(MyPropertyLocators.main_usage_dropdown).choose_option(main_usage)

    def get_main_usage(self) -> str:
        """
        Pobranie głównej użyteczności nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.main_usage_dropdown).get_value()

    def get_main_usage_validation(self) -> str:
        """
        Pobranie tekstu walidacji głównej użyteczności nieruchomości
        :return:
        """
        return self.get_element(MyPropertyLocators.main_usage_dropdown).get_validation()

    def save(self):
        """
        Zapisanie danych
        :return:
        """
        self.get_element(MyPropertyLocators.save_button).click()
        self.wait_for_element(MyPropertyLocators.property_name_input, timeout=10)

    def cancel(self):
        """
        Anulowanie danych
        :return:
        """
        self.get_element(MyPropertyLocators.cancel_button).click()

    def _structure_table(self) -> Table:
        """
        Pobranie komponentu tabeli
        :return: sterownik tabeli
        """
        return self.get_component(MyPropertyLocators.structure_table)

    def get_structure_table(self, empty_table: bool = False) -> dict:
        """
        Pobranie tabeli struktury jako słownika
        :return:
        """
        if empty_table:
            return self._structure_table().get_table()
        else:
            return self._structure_table().get_table(unique_column_name='NAME')

# TODO dodanie obsługi akcji w tabeli
    def delete_structure(self, structure: str):
        return self._structure_table().delete_row(row_name=structure)

    def duplicate_structure(self, structure: str):
        return self._structure_table().duplicate_row(row_name=structure, confirmation=True)

    def add_new_structure(self) -> AddToStructureModal:
        self.get_element(MyPropertyLocators.add_structure_button).click()
        return AddToStructureModal(self.driver)

    def modal_is_displayed(self):
        self.get_element(MyPropertyLocators)
