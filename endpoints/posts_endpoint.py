import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class PostsEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все должности")
    def get_all_posts(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.post_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем id всех должностей")
    def get_all_posts_id(self):
        all_posts = self.get_all_posts().json()
        posts_id = []
        for post in all_posts:
            posts_id.append(post['id'])
        return posts_id
