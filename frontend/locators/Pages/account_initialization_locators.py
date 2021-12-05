class AccountInitializationLocators:
    company_input = "//span[@id='first_time_admin_login_company']", 'Input'
    role_input = "//span[@id='first_time_admin_login_rolename']", 'Input'
    first_name_input = "//span[@id='first_time_login_firstname']", 'Input'
    last_name_input = "//span[@id='first_time_login_lastname']", 'Input'
    initials_input = "//span[@id='first_time_login_initials']", 'Input'
    email_input = "//span[@id='first_time_login_email']", 'Input'
    phone_input = "//span[@id='first_time_login_tel']", 'Input'
    save_button = "//button[@id='first_time_login_submit']", "Button"
    cancel_button = "//button[@id='first_time_login_cancel']", "Button"
    password_input = "", "Input"  # Bug - NOT implemented
    password_confirmation_input = "", "Input"  # Bug - NOT implemented
