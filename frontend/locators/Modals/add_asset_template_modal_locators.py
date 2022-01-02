class AddAssetTemplateLocators:
    template_name_input = "//*[@id='name']", "Input"
    template_type_dropdown = "//*[@id='blockType']", "Dropdown"
    tags_component = "(//div[@class='ReactModalPortal']//div[contains(@class,'grid-cell')])[8]", "Tags"
    icons_component = "(//div[@class='ReactModalPortal']//div[contains(@class,'grid-cell')])[9]", "Icons"
