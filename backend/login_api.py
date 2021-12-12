import json

from backend.Base_API_handler import BaseAPI


class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.role = 'role'
        self.user = 'user'
        self.factory_reset = 'device/factoryreset'

    def get_init_done(self) -> bool:
        """
        Sprawdzenie czy inicjacja została wykonana
        :return: True jeśli inicjacja została wykonana, False jeśli nie
        """
        return True if self.send_request('get', self.init_done)['status'] == 'StructureInitializationDone' else False

    # def get_myself(self):
    #     """
    #     Pobranie danych zalogowanego użytkownika
    #     :return: wartość żądania get /user/myself
    #     """
    #     return self.send_request('get', self.myself)

    def get_roles(self):
        roles = self.send_request('get', self.role)
        roles_dict: dict = {}
        for role in roles:
            roles_dict[role['name']] = role
        return roles_dict

    def get_all_users(self) -> dict:
        """
        Return all users as dict with name key
        :return:
        """
        users = self.send_request('get', self.user)
        users_dict: dict = {}
        for user in users:
            users_dict[user['name']] = user
        return users_dict

    def get_user_details(self, user_id: str) -> dict:
        """
        Return dict with user details
        :param user_id:
        :return:
        """
        return self.send_request('get', self.user + f'/{user_id}')

    def post_create_user(self, user_data: dict):
        """
        Create a new local user in the system
        Pobranie danych zalogowanego użytkownika
        :return: wartość żądania get /user/myself
        """
        roles = self.get_roles()
        admin_type_id = roles['System Administrator']['id']
        # for role in roles:
        #     if role['name'] == 'System Administrator':
        #         admin_type_id = role['id']
        #         continue
        #     else:
        #         admin_type_id = role['id']
        #         continue
        if user_data['roleIds'][0] != admin_type_id:
            user_data['roleIds'][0] = admin_type_id
        if 'tags' in user_data.keys():
            user_data['tags'][0] = f'bos:profile_company_id:{admin_type_id}'
        data = json.dumps(user_data)
        return self.send_request('post', self.user, data=data)

    def put_initialize_account_data(self, name: str, user_data: dict):
        """
        Update an existing local user in the system
        :return:
        """
        roles = self.get_roles()
        user_data['roleIds'] = [roles['System Administrator']['id']]
        users = self.get_all_users()
        user_id = users[name]['id']
        data = json.dumps(user_data)
        return self.send_request('put', self.user+f'/{user_id}', data=data)

    def post_factory_rest(self):
        """
        Executes factory reset
        :return:
        """
        self.send_request('post', self.factory_reset)
