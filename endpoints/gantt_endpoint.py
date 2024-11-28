import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class GanttEndpoint:
    response = None
    response_json = None

    @allure.step("Создание задачи")
    def create_task(self, project_id,json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls().gantt_url + f'?projectId={project_id}', headers=header, json=json, verify=False)
        return self.response

    @allure.step('Переход в режим редактирования')
    def start_editing(self, project_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls().gantt_start_editing_url + f'?projectId={project_id}', headers=header, verify=False)
        return self.response

    @allure.step('Переход в режим редактирования под другим пользователем')
    def start_editing_by_other_user(self, project_id):
        payload = dict(
            login='superadmin',
            password='password',
        )
        AuthEndpoint().auth_api(payload)
        header = AuthEndpoint().get_header_token_by_other_user(payload)
        self.response = requests.post(url=Urls().gantt_start_editing_url + f'?projectId={project_id}', headers=header,
                                      verify=False)
        return self.response

    @allure.step('Изменение статуса фазы')
    def change_stage_status(self, stage_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls().gantt_stage_status_url.replace('{id}', str(stage_id)), json=json, headers=header, verify=False)
        return self.response

    @allure.step('Изменение статуса задачи')
    def change_task_status(self, stage_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls().gantt_task_status_url.replace('{id}', str(stage_id)), json=json, headers=header, verify=False)
        return self.response

    @allure.step('Получение всех задач на проекте')
    def get_all_tasks(self, project_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(Urls().gantt_tasks_url + f'?projectId={project_id}', headers=header, verify=False)
        return self.response
