import requests

from data.urls import Urls

class ProjectRolesApi:

    def get_project_roles_api(self, header):
        response = requests.get(url=Urls.project_role_url, headers=header).json()
        return len(response)

    def post_project_roles_api(self, header):
        payload = {
            "name": "Тестировщик автоматизатор"
        }
        response = requests.post(url=Urls.project_role_url, headers=header, json=payload)

