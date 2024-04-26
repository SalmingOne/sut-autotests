import allure
import requests

from data.urls import Urls

from endpoints.auth_endpoint import AuthEndpoint


class UserEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем id пользователя по электронной почте")
    def get_user_id_by_email(self, email):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.users_url, headers=header)
        self.response_json = self.response.json()
        for user in self.response_json:
            if user['email'] == email:
                return user['id']

    @allure.step("Изменяем пользователя")
    def change_user(self, user_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(url=Urls.users_url + user_id, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем пользователя по id")
    def get_user_by_id(self, user_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.users_url + user_id, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем фамилии пользователей без проектов и с одной проектной ролью")
    def get_users_whit_one_project_role_and_no_assignments(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.users_url, headers=header)
        self.response_json = self.response.json()
        data = []
        for user in self.response_json:
            if len(user["projectRoles"]) == 1 and len(user["assignments"]) == 0:
                data.append(user["secondName"] + ' ' + user["name"])
        return data

    @allure.step("Создание пользователя")
    def create_user_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.users_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получение id пользователя по логину")
    def get_user_id_by_login_api(self, username):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.users_url, headers=header)
        self.response_json = self.response.json()
        for user in self.response_json:
            if user['username'] == username:
                return user['id']