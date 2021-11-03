from backend.Base_API_handler import BaseAPI


class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.init_done = 'initialization'
        self.myself = 'user/myself'
        self.role = 'role'
        self.user = 'user'

    def get_init_done(self) -> bool:
        """
        Sprawdzenie czy inicjacja została wykonana
        :return: True jeśli inicjacja została wykonana, False jeśli nie
        """
        return True if self.send_request('get', self.init_done)['status'] == 'StructureInitializationDone' else False

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

    def get_roles(self):
        return self.send_request('get', self.role)

    def post_create_user(self, user_data: dict):
        """
        Pobranie danych zalogowanego użytkownika
        :return: wartość żądania get /user/myself
        """
        roles = self.get_roles()
        for role in roles:
            if role['name'] == 'System Administrator':
                admin_type_id = role['id']
                continue
        if user_data['roleIds'][0] != admin_type_id:
            user_data['roleIds'][0] = admin_type_id
            user_data['tags'][0] = [f'bos:profile_company_id:{admin_type_id}']
        return self.send_request('post', self.user)
