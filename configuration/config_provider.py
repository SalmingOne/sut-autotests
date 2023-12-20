import configparser
from pathlib import PurePath


class ConfigProvider:
    config_dir = str(PurePath(__file__).parent.parent) + '\\config.ini'

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(self.config_dir)

    def get_project_url(self) -> str:
        return self.config["api"].get(
            "base_url") + self.config["api"].get("projects_url")

    def get_auth_url(self) -> str:
        return self.config["api"].get(
            "base_url") + self.config["api"].get("auth_url")

    def get_admin_creds(self) -> dict:
        return {
            "login": self.config["creds"].get("login"),
            "password": self.config["creds"].get("password")
        }

    def set_token(self, token) -> None:
        self.config.set("api", "token", token)
        with open(self.config_dir, 'w') as configfile:
            self.config.write(configfile)

    def get_token(self) -> str:
        return self.config["api"].get("token")

    def get_token_as_dict_for_headers(self) -> dict:
        return {"Access": "Bearer " + self.get_token()}

    def get_system_settings_url(self):
        return self.config["api"].get("base_url") + self.config["api"].get("system_settings_url")
