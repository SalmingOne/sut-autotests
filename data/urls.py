
import os
from dotenv import load_dotenv

load_dotenv()


class Urls:
    base_url = os.getenv('BASE_URL')
    api_url = f'{base_url}' + 'api/'
    auth_url = f'{api_url}' + 'auth/'
    project_url = f'{api_url}' + 'projects/'
    system_roles_url = f'{api_url}' + 'system-roles/'
    department_url = f'{api_url}' + 'departments/'
    post_url = f'{api_url}' + 'posts/'
    project_role_url = f'{api_url}' + 'project-roles/'
    affiliates_url = f'{api_url}' + 'affiliates/'
    users_url = f'{api_url}' + 'users/'
    labor_reports_url = f'{api_url}' + 'labor-reports/'
    assignment_url = f'{api_url}' + 'assignments/'
    variables_url = f'{api_url}' + 'variables/'
    logs_url = f'{api_url}' + 'logs/'
    logs_settings_url = f'{logs_url}' + 'settings/'
    tags_url = f'{api_url}' + 'tags/'
    skills_url = f'{api_url}' + 'skills/'
    system_settings_url = f'{api_url}' + 'system-settings/'
    advanced_search_url = f'{api_url}' + 'search/'
    create_advanced_search_url = f'{advanced_search_url}' + 'create/'
    resume_url = f'{api_url}' + 'resume/'

