from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    IN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
