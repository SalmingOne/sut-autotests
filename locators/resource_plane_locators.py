from selenium.webdriver.common.by import By

from data.data import USER_NAME


class ResourcePlaneLocators:
    # Переход на страницу Ресурсный план
    PLANING_MORE = (By.CSS_SELECTOR, 'div[id="planning"]')
    TAB_RESOURCE_PLANE = (By.CSS_SELECTOR, 'a[href="/resource-plan-table/projects"]')

    def project_color_on_user(self, project_code):
        return (By.XPATH, f'//p[text()="{project_code}"]')

    def project_color_on_project(self, project_code):
        return (By.XPATH, f'//span[text()="{project_code}"]')

    # Отображение по пользователю
    BY_USER_BUTTON = (By.XPATH, '//button[text()="По пользователям"]')
    OPEN_PROJECT_LIST = (By.XPATH, f'//span[contains(@aria-label,"{USER_NAME}")]')
    ROLE_FILTER_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Начните вводить роль"]')

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
