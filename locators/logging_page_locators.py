from selenium.webdriver.common.by import By


class LoggingPageLocators:
    # Переход на страницу логирования
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_AUDIT_TAB = (By.CSS_SELECTOR, 'a[href="/admin/settings/audit"]')
    # Поля и кнопки на странице логирования
    AUDIT_STATUS_FIELD = (By.XPATH, '//div[@name="status"]//input')
    AUDIT_LEVEL_FIELD = (By.XPATH, '//div[@name="level"]//input')
    DEPTH_DATE_QUANTITY_FIELD = (By.CSS_SELECTOR, 'input[name="depthDateQuantity"]')
    DEPTH_DATE_TYPE_FIELD = (By.XPATH, '//div[@name="depthDateType"]//input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Поля и кнопки на модальном окне
    DIALOG_TEXT = (By.CSS_SELECTOR, 'p[class^="MuiTypography-root MuiTypography-body2"]')
    DIALOG_SUBMIT_BUTTON = (By.XPATH, '//div[@role="dialog"]//button[@type="submit"]')
    DIALOG_ABORT_BUTTON = (By.XPATH, '//div[@role="dialog"]//button[contains(@class,"MuiButton-outlinedSizeSmall MuiButton-disableElevation")]')
    # Сообщения системы
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    # Пункт меню Аудит
    AUDIT_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/logging"]')
    ELEMENTS_IN_SELECT = (By.XPATH, "//li")
    # Выбор пункта меню
    def set_choice(self, choice):
        return (By.XPATH, f'//li[text()="{choice}"]')

