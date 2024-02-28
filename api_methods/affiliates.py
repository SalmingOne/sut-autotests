import requests

from configuration.config_provider import ConfigProvider

config = ConfigProvider()


class AffiliatesApi:

    def get_affiliates_api(self, token):
        response = requests.get(url=config.get_project_url() + 'affiliates', headers={"Access": "Bearer " + token}).json()
        return len(response)

    def post_affiliates_api(self, token):
        payload = {
            "name": "Саратовский филиал",
            "address": None
        }
        response = requests.post(url=config.get_project_url() + 'affiliates', headers={"Access": "Bearer " + token},
                                 json=payload)

