from backend.Base_API_handler import BaseAPI


class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.init_done = 'initialization'
        self.myself = 'user/myself'

    def get_init_done(self) -> bool:
        """
        Sprawdzenie czy inicjacja została wykonana
        :return: True jeśli inicjacja została wykonana, False jeśli nie
        """
        return True if self.send_request('get', self.init_done)['status'] == "CoreInitializationDone" else False

    def get_initialization_status(self) -> str:
        """
        Pobranie statusu inicjacji Admina
        :return:
        """
        return self.send_request('get', self.init_done)['status']

    def get_myself(self):
        """
        Pobranie danych zalogowanego użytkownika
        :return: wartość żądania get /user/myself
        """
        return self.send_request('get', self.myself)

