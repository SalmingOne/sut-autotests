from selenium.webdriver.common.by import By


class UserProfilePageLocators:
    # Переход на страницу профиля
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'button[id="profile"]')
    MY_PROFILE_MENU_ITEM = (By.XPATH, '//a[text()="Мой профиль"]')
    # Вкладка Образование
    EDUCATION_TAB_BUTTON = (By.XPATH, '//button[text()="Образование"]')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    ADD_ICON = (By.CSS_SELECTOR, 'button[aria-label="Нажмите, чтобы добавить новую карточку"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    # Вкладка Сертификаты
    CERTIFICATE_TAB_BUTTON = (By.XPATH, '//button[text()="Сертификаты"]')

