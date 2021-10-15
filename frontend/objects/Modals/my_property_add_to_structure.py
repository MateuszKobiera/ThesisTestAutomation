from selenium import webdriver

from frontend.Locators.Modals.add_structure_modal_locators import AddToStructureLocators
from frontend.objects.Modals.base_modal import BaseModal


class AddToStructureModal(BaseModal):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        
    def set_element_type(self, element_type: str) -> None:
        """
        Ustawienie typu struktury
        :param element_type: Typ struktury
        :return:
        """
        self.get_element(AddToStructureLocators.element_type_dropdown).choose_option(element_type)

    def get_element_type(self) -> str:
        """
        Pobranie typu struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.element_type_dropdown).get_value()

    def get_element_type_validation(self) -> str:
        """
        Pobranie tekstu walidacji typu struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.element_type_dropdown).get_validation()
    
    def set_name(self, name_type: str) -> None:
        """
        Ustawienie nazwy struktury
        :param name_type: Nazwa struktury
        :return:
        """
        self.get_element(AddToStructureLocators.name_input).choose_option(name_type)

    def get_name(self) -> str:
        """
        Pobranie nazwy struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.name_input).get_value()

    def get_name_validation(self) -> str:
        """
        Pobranie tekstu walidacji nazwy struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.name_input).get_validation()
    
    def set_usage(self, usage_type: str) -> None:
        """
        Ustawienie użytku struktury
        :param usage_type: Użytek struktury
        :return:
        """
        self.get_element(AddToStructureLocators.usage_dropdown).set_value(usage_type)

    def get_usage(self) -> str:
        """
        Pobranie użytku struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.usage_dropdown).get_value()

    def get_usage_validation(self) -> str:
        """
        Pobranie tekstu walidacji użytku struktury
        :return:
        """
        return self.get_element(AddToStructureLocators.usage_dropdown).get_validation()
    
    def set_people_quantity(self, people_quantity: str) -> None:
        """
        Ustawienie liczby osób w strukturze
        :param people_quantity: Liczba osób w strukturze
        :return:
        """
        self.get_element(AddToStructureLocators.people_input).choose_option(people_quantity)

    def get_people_quantity(self) -> str:
        """
        Pobranie liczby osób w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.people_input).get_value()

    def get_people_quantity_validation(self) -> str:
        """
        Pobranie tekstu walidacji liczby osób w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.people_input).get_validation()
    
    def set_gross_surface(self, gross_surface: str) -> None:
        """
        Ustawienie powierzchni brutto w strukturze
        :param gross_surface: Powierzchnia brutto w strukturze
        :return:
        """
        self.get_element(AddToStructureLocators.gross_surface_input).choose_option(gross_surface)

    def get_gross_surface(self) -> str:
        """
        Pobranie powierzchni brutto w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.gross_surface_input).get_value()

    def get_gross_surface_validation(self) -> str:
        """
        Pobranie tekstu walidacji powierzchni brutto w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.gross_surface_input).get_validation()
    
    def set_net_surface(self, net_surface: str) -> None:
        """
        Ustawienie powierzchni netto w strukturze
        :param net_surface: Powierzchnia netto w strukturze
        :return:
        """
        self.get_element(AddToStructureLocators.net_surface_input).choose_option(net_surface)

    def get_net_surface(self) -> str:
        """
        Pobranie powierzchni netto w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.net_surface_input).get_value()

    def get_net_surface_validation(self) -> str:
        """
        Pobranie tekstu walidacji powierzchni netto w strukturze
        :return:
        """
        return self.get_element(AddToStructureLocators.net_surface_input).get_validation()

    def set_element_in_building(self, building_name: str) -> None:
        """
        Ustawienie budynku dla elementu innego typu
        :param building_name: Budynek w którym znajduje się element struktury
        :return:
        """
        self.get_element(AddToStructureLocators.in_building_dropdown).choose_option(building_name)

    def get_element_in_building(self) -> str:
        """
        Pobranie budynku dla elementu innego typu
        :return:
        """
        return self.get_element(AddToStructureLocators.in_building_dropdown).get_value()

    def get_element_in_building_validation(self) -> str:
        """
        Pobranie tekstu walidacji budynku dla elementu innego typu
        :return:
        """
        return self.get_element(AddToStructureLocators.in_building_dropdown).get_validation()

    def set_level_to_ground(self, level_to_ground: str) -> None:
        """
        Ustawienie piętra dla elementu
        :param level_to_ground: Piętro dla elementu
        :return:
        """
        self.get_element(AddToStructureLocators.level_to_ground_input).choose_option(level_to_ground)

    def get_level_to_ground(self) -> str:
        """
        Pobranie piętra dla elementu
        :return:
        """
        return self.get_element(AddToStructureLocators.level_to_ground_input).get_value()

    def get_level_to_ground_validation(self) -> str:
        """
        Pobranie tekstu walidacji piętra dla elementu
        :return:
        """
        return self.get_element(AddToStructureLocators.level_to_ground_input).get_validation()

