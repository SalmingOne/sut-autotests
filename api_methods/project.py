import requests
import allure
import data.data
from configuration.config_provider import ConfigProvider
from api_methods.auth import AuthApi


config = ConfigProvider()


class ProjectApi:


    @allure.step("Создать проект с помощью API")
    def create_project(
            self,
            code: str = data.data.VALID_PROJECT_DATA["code"],
            name: str = data.data.VALID_PROJECT_DATA["name"],
            startDate: str = data.data.VALID_PROJECT_DATA["startDate"],
            status: str = data.data.VALID_PROJECT_DATA["status"],
            selfAdding: bool = data.data.VALID_PROJECT_DATA["selfAdding"],
            laborReasons: bool = data.data.VALID_PROJECT_DATA["laborReasons"],
            mandatoryAttachFiles: bool = data.data.VALID_PROJECT_DATA["mandatoryAttachFiles"],
            description: dict = data.data.VALID_PROJECT_DATA["description"],
            endDate: str = data.data.VALID_PROJECT_DATA["endDate"],
            fileDescription: dict = data.data.VALID_PROJECT_DATA["fileDescription"],
            automaticLaborReports: bool = data.data.VALID_PROJECT_DATA["automaticLaborReports"],
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
        token = AuthApi().auth_to_token()
        response = requests.post(
            url=config.get_project_url(),
            headers={"Access": "Bearer " + token},
            json={
                "code": code,
                "name": name,
                "startDate": startDate,
                "status": status,
                "selfAdding": selfAdding,
                "laborReasons": laborReasons,
                "mandatoryAttachFiles": mandatoryAttachFiles,
                "description": description,
                "endDate": endDate,
                "fileDescription": fileDescription,
                "automaticLaborReports": automaticLaborReports,
                "resources": resources
            }

        )
        return response.json()

    @allure.step("Удалить проект с id {id} помощью API")
    def delete_project(self, id: int):
        token = AuthApi().auth_to_token()
        assert requests.delete(
            url=config.get_project_url() + str(id),
            headers={"Access": "Bearer " + token}
        ).status_code == 204
