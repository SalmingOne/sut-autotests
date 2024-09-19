from selenium.webdriver.common.by import By

class TemplatePageLocators:
    # Переход на страницу Шаблоны
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM = (By.XPATH, '//a[text()="Система"]')
    TEMPLATE_TAB = (By.XPATH, '//button[text()="Шаблоны"]')
    # Блок с шаблонами
    DELETE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ADD_DOC = (By.CSS_SELECTOR, 'input[type="file"]')
    #Блок с переменными
    CREATE_VARIABLE = (By.XPATH, '//button[text()="Создать переменную"]')
    FIELD_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    VARIABLE_NAME = (By.CSS_SELECTOR, 'input[name="systemName"]')
    VARIABLE_VALUE = (By.CSS_SELECTOR, 'input[name="value"]')
    TEMPLATE_WITH_VARIABLE = (By.CSS_SELECTOR, 'svg[data-testid="ArrowDropDownIcon"]')
    TEMPLATE_VALUE = (By.XPATH, '//li[text()="Ежегодный отпуск"]')
    VALUE_FROM_COLUMN_TEMPLATE = (By.XPATH, '//div[text()="Ежегодный отпуск"]')
    DELETE = (By.XPATH, '//span[text()="Удалить"]')

    def check_text(self, text):
        return (By.XPATH, f'//*[text()="{text}"]')

    def get_value_from_column(self, variable_name, column_number):
        return (By.XPATH, f'//div[@aria-label="{variable_name}"]//ancestor::div[contains(@class,"ag-row-even ag-row-no-focus")]//div[@aria-colindex="{column_number}"]//div')
