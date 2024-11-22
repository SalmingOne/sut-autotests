import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class SystemRolesEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все системные роли")
    def get_all_system_roles(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.system_roles_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем id всех системных ролей")
    def get_all_system_roles_id(self):
        all_system_roles = self.get_all_system_roles().json()
        system_roles_id = []
        for role in all_system_roles:
            system_roles_id.append(role['id'])
        return sorted(system_roles_id)

    @allure.step("Получаем id системной роли по имени")
    def get_user_system_role_id(self, name):
        all_system_roles = self.get_all_system_roles().json()
        for role in all_system_roles:
            if role['name'] == name:
                return role['id']
            
    @allure.step("Получаем полномочия системной роли по id")
    def get_tags_system_role_id(self, system_role_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.system_roles_url + f'{system_role_id}', headers=header, verify=False)
        all_tags = self.response.json()['authority']
        result = [{'id': d['id'], 'systemTagId': d['systemTagId'], 'action': d['action'], 'ownData': d['ownData']} for d in all_tags]
        return result
    
    @allure.step("Удаляем системную роль по id")
    def delete_system_role_id(self, system_role_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.system_roles_url + f'{system_role_id}', headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response
