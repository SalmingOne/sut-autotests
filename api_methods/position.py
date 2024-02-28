import requests

from configuration.config_provider import ConfigProvider
config = ConfigProvider()

class PositionsApi:

    def get_positions_api(self, token):
        response = requests.get(url=config.get_project_url() + 'posts', headers={"Access": "Bearer " + token}).json()
        return len(response)

    def post_positions_api(self, token):
        payload = {
            "name": "Специалист эксперт"
        }
        response = requests.post(url=config.get_project_url() + 'posts', headers={"Access": "Bearer " + token}, json=payload)
