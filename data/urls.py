from configuration.config_provider import ConfigProvider


class Urls:
    config = ConfigProvider()
    base_url = config.get_base_url()
    url = base_url[:-4]
    auth_url = f'{base_url}' + 'auth/'
    project_url = f'{base_url}' + 'projects/'
    system_roles_url = f'{base_url}' + 'system-roles/'
    department_url = f'{base_url}' + 'departments/'
    post_url = f'{base_url}' + 'posts/'
    project_role_url = f'{base_url}' + 'project-roles/'
    affiliates_url = f'{base_url}' + 'affiliates/'
    users_url = f'{base_url}' + 'users/'
    labor_reports_url = f'{base_url}' + 'labor-reports/'
    assignment_url = f'{base_url}' + 'assignment/'
    variables_url = f'{base_url}' + 'variables/'
