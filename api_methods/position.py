import requests

from data.urls import Urls


class PositionsApi:

    def get_positions_api(self, header):
        response = requests.get(url=Urls.post_url, headers=header).json()
        return len(response)

    def post_positions_api(self, header):
        payload = {
            "name": "Специалист эксперт"
        }
        response = requests.post(url=Urls.post_url, headers=header, json=payload)
