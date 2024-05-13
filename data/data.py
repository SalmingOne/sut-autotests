import os
from dotenv import load_dotenv

from endpoints.users_endpoint import UserEndpoint

load_dotenv()
user_endpoint = UserEndpoint()

PROJECT_NAME = "AutoTestProject"
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
USER_NAME = user_endpoint.get_user_id_and_name_by_login(LOGIN)[1]
USER_ID = user_endpoint.get_user_id_and_name_by_login(LOGIN)[0]
