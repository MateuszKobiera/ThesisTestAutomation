from selenium import webdriver

from frontend.components.base_component import BaseComponent


class Icons(BaseComponent):
    def __init__(self, driver: webdriver, xpath):
        super().__init__(driver)
        self.xpath = xpath

    def clear_icons(self) -> None:
        """
        Clicks on Clear button to clear icon and background
        """
        clear_button = self.xpath + "//div[@title='Delete current definition']"
        self.get_element((clear_button, "Button")).click()

    def set_background(self, color_type: str, color: (tuple, str)) -> None:
        """
        Ustawienie tła dla ikony
        :return: nic nie zwraca
        """
        clear_button = self.xpath + "//div[@title='Pick a background color']"
        self.get_element((clear_button, "Button")).click()
        self.wait_for_element(clear_button + '/div[2]')
        input_xpath = clear_button + "//label[text()='{}']/preceding-sibling::input"
        change_input_type_xpath = clear_button + "/div[2]//*[name()='svg']"
        color_types = 0
        if color_type.lower() == 'hex':
            if type(color) == str:
                while self.check_is_element_visible((input_xpath.format('hex'), "Input")) is False and color_types < 3:
                    self.get_element(change_input_type_xpath).click()
                    color_types += 1
                    if color_types >= 3:
                        ValueError('HEX color type input was not found')
                self.get_element((input_xpath.format('hex'), "Input")).set_value(color)
            else:
                raise TypeError(f'Wrong type of color argument, there is {type(color)}, but should be str for hex.')
        elif color_type.lower() == 'rgb':
            if type(color) == tuple:
                while self.check_is_element_visible((input_xpath.format('r'), "Input")) is False and color_types < 3:
                    self.get_element(change_input_type_xpath).click()
                    color_types += 1
                    if color_types >= 3:
                        ValueError('HEX color type input was not found')
                self.get_element((input_xpath.format('r'), "Input")).set_value(color[0])
                self.get_element((input_xpath.format('g'), "Input")).set_value(color[1])
                self.get_element((input_xpath.format('b'), "Input")).set_value(color[2])
            else:
                raise TypeError(f'Wrong type of color argument, there is {type(color)}, but should be tuple for rgb.')
        elif color_type.lower() == 'hsl':
            if type(color) == tuple:
                while self.check_is_element_visible((input_xpath.format('h'), "Input")) is False and color_types < 3:
                    self.get_element(change_input_type_xpath).click()
                    color_types += 1
                    if color_types >= 3:
                        ValueError('HSL color type input was not found')
                self.get_element((input_xpath.format('h'), "Input")).set_value(color[0])
                self.get_element((input_xpath.format('s'), "Input")).set_value(color[1])
                self.get_element((input_xpath.format('l'), "Input")).set_value(color[2])
            else:
                raise TypeError(f'Wrong type of color argument, there is {type(color)}, but should be tuple for hsl.')
        else:
            ValueError('There is no such color_type_input. You can choose between: "hex", "rgb", "hsl".')
        self.get_element(("//html", "Button")).click()

    def get_background_color(self):
        color = self.get_element((self.xpath + "/div/div[1]", "Base")).driver.value_of_css_property("background-color")
        return tuple(color.split('(')[1].split(',')[:-1])

    def set_icon(self, number_of_icon: int):
        """
        Set an icon to be displayed
        :param number_of_icon: number of icon index
        :return: nic nie zwraca
        """
        select_icon_button = self.xpath + "//div[@title='Pick or import a symbol']"
        self.get_element((select_icon_button, "Button")).click()
        self.wait_for_element(select_icon_button + '/div')
        self.get_element((select_icon_button + f"/div/div/div[2]/div[{number_of_icon}]", "Button")).click()


