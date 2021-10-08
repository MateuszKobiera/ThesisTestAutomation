from frontend.Locators.login_page import LoginPageLocators


def test_initialization_with_login(login_page):
    login_page.wait_for_element(LoginPageLocators.login_button)
    assert login_page.login_url == login_page.driver.current_url