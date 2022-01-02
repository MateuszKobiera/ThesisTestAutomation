class AssetTemplatesLocators:
    active_tab = "//*[contains(@class,'active')]", "Button"
    add_template = "//*[text()='{}']/ancestor::span//button", 'Button'
    template_table = "//*[text()='{}']/ancestor::span//table", "Table"
    master_slave_switcher = "//*[@id='supportMasterSlave']", 'Switcher'
    add_datapoint_button = "//*[text()='Add datapoint']//ancestor::button", "Button"
    add_property_button = "//*[text()='Add property']//ancestor::button", "Button"
    point_properties_table = "//table[contains(@class,'small')]", "Table"
    tags_component = "(//div[contains(@class,'TabControl__activeContent')])[last()]/div/div[last()]", "Tags"