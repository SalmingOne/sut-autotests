from selenium.webdriver.common.by import By


class UserPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')

    def user_by_name(self, name):
        return (By.XPATH, f'//div[contains(@aria-label, "{name}")]')
