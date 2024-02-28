import requests

from configuration.config_provider import ConfigProvider

config = ConfigProvider()
class ProjectRolesApi:

    def get_project_roles_api(self, token):
        response = requests.get(url=config.get_project_url() +'project-roles', headers={"Access": "Bearer " + token}).json()
        return len(response)
    def post_project_roles_api(self, token):
        payload = {
            "name": "Тестировщик автоматизатор"
        }
        response = requests.post(url=config.get_project_url() + 'project-roles', headers={"Access": "Bearer " + token}, json=payload)

