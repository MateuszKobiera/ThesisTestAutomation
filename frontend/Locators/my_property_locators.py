class MyPropertyLocators:
    property_name_input = '//*[@id="overview-tab_site-name"]', "Input"
    address_input = '//*[@id="overview-tab_address-1"]', "Input"
    zip_code_input = '//*[@id="overview-tab_zipCode"]', "Input"
    town_input = '//*[@id="overview-tab_town"]', "Input"
    gross_surface_input = '//*[@id="overview-tab_gross-surface"]', "Input"
    people_input = '//*[@id="overview-tab_people"]', "Input"
    gps_latitude_input = '//*[@id="gpslat"]', "Input"
    gps_longitude_input = '//*[@id="gpslon"]', "Input"
    country_dropdown = '//*[@id="overview-tab_country"]', "Dropdown"
    property_type_dropdown = '//*[@id="overview-tab_type"]', "Dropdown"
    main_usage_dropdown = '//*[@id="overview-tab_main-usage"]', "Dropdown"
    property_image = '//*[@id="overview-tab_image"]', "Base"  # TODO handle image
    get_coordinates_button = '//*[@id="overview-tab_get-gps"]', "Button"
    save_button = "//span[text()='Save']//ancestor::button", "Button"
    cancel_button = "//span[text()='Cancel']//ancestor::button", "Button"
    structure_table = "//table", "Table"


