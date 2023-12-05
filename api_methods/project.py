import requests
import allure
import data.data
from configuration.config_provider import ConfigProvider
from api_methods.auth import AuthApi


config = ConfigProvider()


class ProjectApi:

    def __init__(self):
        AuthApi().auth()

    @allure.step("Создать проект с помощью API")
    def create_project(
            self,
            code: str = data.data.VALID_PROJECT_DATA["code"],
            name: str = data.data.VALID_PROJECT_DATA["name"],
            startDate: str = data.data.VALID_PROJECT_DATA["startDate"],
            status: str = data.data.VALID_PROJECT_DATA["status"],
            laborReasons: bool = data.data.VALID_PROJECT_DATA["laborReasons"],
            mandatoryAttachFiles: bool = data.data.VALID_PROJECT_DATA["mandatoryAttachFiles"],
            description: dict = data.data.VALID_PROJECT_DATA["description"],
            endDate: str = data.data.VALID_PROJECT_DATA["endDate"],
            fileDescription: dict = data.data.VALID_PROJECT_DATA["fileDescription"],
            resources: list = data.data.VALID_PROJECT_DATA["resources"]):
        """ Создание проекта через API

        :param code: код проекта (обязательное)

        :param name: название проекта (обязательное)

        :param startDate: дата начала проекта (обязательное)

        :param status: статус проекта (ACTIVE, ARCHIVED, DRAFT) (обязательное)

        :param laborResons: чекбокс "Обязательность указания причин списания трудозатрат" (обязательное)

        :param mandatoryAttachFiles: чекбокс "Обязательность приложения файлов при переработках и отпусках" (обязательное)


        :param description: описание проекта, словарь {
            "description" : текст поддерживающий маркдауны обёрнутый в JSON (пример в data.py)
        }

        :param endDate: дата окончания проекта

        :param fileDescription: описание файлов прилагаемых к переработке, словарь {
            "description" : текст поддерживающий маркдауны обёрнутый в JSON (пример в data.py)
        }

        :param resources: список словарей [{
            "projectRoleId" : проектная роль ресурса
            "userId" : id ресурса
            "isProjectManager" : менеджер проекта (Boolean)
        }]
        """

        response = requests.post(
            url=config.get_project_url(),
            headers=config.get_token_as_dict_for_headers(),
            json={
                "code": code,
                "name": name,
                "startDate": startDate,
                "status": status,
                "laborReasons": laborReasons,
                "mandatoryAttachFiles": mandatoryAttachFiles,
                "description": description,
                "endDate": endDate,
                "fileDescription": fileDescription,
                "resources": resources
            }
        )
        return response.json()

    @allure.step("Удалить проект с id {id} помощью API")
    def delete_project(self, id: int):
        assert requests.delete(
            url=config.get_project_url() + str(id),
            headers=config.get_token_as_dict_for_headers()
        ).status_code == 204
