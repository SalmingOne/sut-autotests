import os
from dotenv import load_dotenv

from user_id_and_name import ID, USER_NAME

load_dotenv()


PROJECT_NAME = "AutoTestProject"
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
USER_NAME = USER_NAME
USER_ID = ID
