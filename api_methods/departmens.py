import requests

from data.urls import Urls


class DepartmentsApi:

    def get_departments_api(self, header):
        response = requests.get(url=Urls.department_url, headers=header).json()
        return len(response)

    def post_department_api(self, header):
        payload = {
            "name": "Первый отдел",
            "departmentId": None
        }
        response = requests.post(url=Urls.department_url, headers=header, json=payload)
