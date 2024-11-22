
import os
from dotenv import load_dotenv

load_dotenv()


class Urls:
    base_url = os.getenv('BASE_URL')
    api_url = f'{base_url}' + 'api/'
    auth_url = f'{api_url}' + 'auth/'
    project_url = f'{api_url}' + 'projects/'
    project_for_current_user_url = f'{api_url}' + 'projects/for-current-user?onlyCurrentProjects=true'
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
    skills_url = f'{api_url}' + 'skills/'
    skills_del_url = f'{api_url}' + 'skills?ids%5B0%5D='
    system_settings_url = f'{api_url}' + 'system-settings/'
    advanced_search_url = f'{api_url}' + 'search/'
    create_advanced_search_url = f'{advanced_search_url}' + 'create/'
    resume_url = f'{api_url}' + 'resume/'
    calendar_url = f'{api_url}' + 'calendar/'
    gantt_url = f'{api_url}' + 'gantt/'
    gantt_tasks_url = gantt_url + 'tasks/'
    gantt_start_editing_url = gantt_url + 'start-editing/'
    gantt_stage_status_url = gantt_url + 'stages/{id}/status/'
    gantt_task_status_url = gantt_url + 'tasks/{id}/status/'
    busy_percentages_url = f'{api_url}' + 'busy-percentages/'
    schedule_url = f'{api_url}' + 'schedule/'
    labels_url = f'{api_url}' + 'labels/'
    personal_quality_url = f'{api_url}' + 'personalQualities/'
    statement_files_url = f'{api_url}' + 'statement-files/'
    files_url = f'{api_url}' + 'files/'
    files_application_template_url = f'{api_url}' + 'files/applicationTemplate/'
    attraction_rates_url = f'{api_url}' + 'attraction-rates/'
    slots_url = f'{api_url}' + 'slots/'

