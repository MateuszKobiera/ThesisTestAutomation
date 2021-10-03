class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def base_url(self):
        return 'http://localhost:3000/'
