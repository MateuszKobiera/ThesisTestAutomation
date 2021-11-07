class AddDatapointPropertyLocators:
    custom_datapoint = "//*[text()='Custom']/..", "Button"
    name_input = "//*[@id='name']", "Input"
    type_dropdown = '//*[@id="direction"]',  "Dropdown"
    format_dropdown = '//*[@id="format"]',  "Dropdown"
    unit_dropdown = '//*[@data-testid="UnitPicker.UnitsDropdown"]',  "Dropdown"
    min_value_input = '//*[@id="min"]', "Input"
    max_value_input = '//*[@id="max"]', "Input"
    display_unit_dropdown = '//*[@id="displayUnitId"]', "Dropdown"
    tags_component = "(//div[@class='ReactModalPortal']//div[contains(@class,'grid-cell')])[last()-1]", "Tags"

