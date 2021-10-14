from selenium import webdriver

from frontend.Locators.my_property_locators import MyPropertyLocators
from frontend.Modals.base_modal import BaseModal


class AddToStructureModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        
    def set_element_type(self, element_type: str) -> None:
        """
        Ustawienie typu struktury
        :param element_type: Typ struktury
        :return:
        """
        self.get_element(MyPropertyLocators.structure_element_type_dropdown).choose_option(element_type)

    def get_element_type(self) -> str:
        """
        Pobranie typu struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_element_type_dropdown).get_value()

    def get_element_type_validation(self) -> str:
        """
        Pobranie tekstu walidacji typu struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_element_type_dropdown).get_validation()
    
    def set_structure_name(self, name_type: str) -> None:
        """
        Ustawienie nazwy struktury
        :param name_type: Nazwa struktury
        :return:
        """
        self.get_element(MyPropertyLocators.structure_name_input).choose_option(name_type)

    def get_structure_name(self) -> str:
        """
        Pobranie nazwy struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_name_input).get_value()

    def get_structure_name_validation(self) -> str:
        """
        Pobranie tekstu walidacji nazwy struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_name_input).get_validation()
    
    def set_structure_usage(self, usage_type: str) -> None:
        """
        Ustawienie użytku struktury
        :param usage_type: Użytek struktury
        :return:
        """
        self.get_element(MyPropertyLocators.structure_usage_dropdown).set_value(usage_type)

    def get_structure_usage(self) -> str:
        """
        Pobranie użytku struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_usage_dropdown).get_value()

    def get_structure_usage_validation(self) -> str:
        """
        Pobranie tekstu walidacji użytku struktury
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_usage_dropdown).get_validation()
    
    def set_structure_people_quantity(self, people_quantity: str) -> None:
        """
        Ustawienie liczby osób w strukturze
        :param people_quantity: Liczba osób w strukturze
        :return:
        """
        self.get_element(MyPropertyLocators.structure_people_input).choose_option(people_quantity)

    def get_structure_people_quantity(self) -> str:
        """
        Pobranie liczby osób w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_people_input).get_value()

    def get_structure_people_quantity_validation(self) -> str:
        """
        Pobranie tekstu walidacji liczby osób w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_people_input).get_validation()
    
    def set_structure_gross_surface(self, gross_surface: str) -> None:
        """
        Ustawienie powierzchni brutto w strukturze
        :param gross_surface: Powierzchnia brutto w strukturze
        :return:
        """
        self.get_element(MyPropertyLocators.structure_gross_surface_input).choose_option(gross_surface)

    def get_structure_gross_surface(self) -> str:
        """
        Pobranie powierzchni brutto w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_gross_surface_input).get_value()

    def get_structure_gross_surface_validation(self) -> str:
        """
        Pobranie tekstu walidacji powierzchni brutto w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_gross_surface_input).get_validation()
    
    def set_structure_net_surface(self, net_surface: str) -> None:
        """
        Ustawienie powierzchni netto w strukturze
        :param net_surface: Powierzchnia netto w strukturze
        :return:
        """
        self.get_element(MyPropertyLocators.structure_net_surface_input).choose_option(net_surface)

    def get_structure_net_surface(self) -> str:
        """
        Pobranie powierzchni netto w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_net_surface_input).get_value()

    def get_structure_net_surface_validation(self) -> str:
        """
        Pobranie tekstu walidacji powierzchni netto w strukturze
        :return:
        """
        return self.get_element(MyPropertyLocators.structure_net_surface_input).get_validation()

