import requests

from configuration.config_provider import ConfigProvider

config = ConfigProvider()

class DepartmentsApi:

    def get_departments_api(self, token):
        response = requests.get(url=config.get_project_url() + 'departments', headers={"Access": "Bearer " + token}).json()
        return len(response)

    def post_department_api(self, token):
        payload = {
              "name": "Первый отдел",
              "departmentId": None
        }
        response = requests.post(url=config.get_project_url() + 'departments', headers={"Access": "Bearer " + token}, json=payload)

