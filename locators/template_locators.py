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

    def check_text(self, text):
        return (By.XPATH, f'//*[text()="{text}"]')