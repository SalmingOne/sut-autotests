from selenium.webdriver.common.by import By

from data import data


class AllProjectPageLocators:
    # Пункты меню для перехода на страницу все проекты
    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')

    # Локатор проверки что имя проекта есть на странице
    CHECK_NAME_PROJECT = (By.XPATH, f'//div[text()="{data.PROJECT_NAME}"]')

    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PROJECT_ACTION_BUTTON = (
        By.XPATH, f'//div[text()="{data.PROJECT_NAME}"]//ancestor::div[contains(@class,"ag-row-odd ag-row")]//button')

    PROJECT_DELETE_BUTTON = (By.XPATH, '//span[text()="Удалить"]')

    PROJECT_STATUS_TEXT = (By.XPATH, f'//div[text()="{data.PROJECT_NAME}"]//ancestor::div[1]//following::span[1]')
    STATUS_FILTER_BUTTON = (By.XPATH, '//span[text()="Статус"]//following::button[5]')



