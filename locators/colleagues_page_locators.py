from selenium.webdriver.common.by import By


class ColleaguesPageLocators:
    # Переход на страницу Коллеги
    COLLEAGUES_TAB = (By.CSS_SELECTOR, 'div[id="colleagues"]')
    ALL_COLLEAGUES = (By.CSS_SELECTOR, 'a[href="/users/department"]')
    # Поля и элементы страницы
    COLLEAGUES_TITLE = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle1"]')
    ALL_COLLEAGUES_TABS_BUTTONS = (By.CSS_SELECTOR, 'button[role="tab"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[class^="MuiOutlinedInput-input MuiInputBase-input"]')
    TO_ADVANCED_SEARCH = (By.XPATH, '//button[text()="Перейти к расширенному поиску"]')
    SUBTITLE = (By.XPATH, '//div[contains(@class,"MuiPaper-elevation0" )]//h6')
    SETTING_ICON = (By.CSS_SELECTOR, 'button[aria-label="Настроить отображение столбцов в таблице"]')
    COLUMN_TITLES = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')
    USER_NAME_LINK = (By.CSS_SELECTOR, 'a[href^="/k"]')
    WATCH_USER_EYES_BUTTONS = (By.CSS_SELECTOR, 'svg[data-testid="VpnKeyIcon"]')
    # Локатор для проверки перехода на страницу пользователя
    CHECK_GO_TO_USER_PAGE = (By.XPATH, '//h6[text()="Общие данные"]')
    # Просмотр глазами пользователя
    RETURN_TO_PROFILE_BUTTON = (By.XPATH, '//button[text()="Вернуться в свой профиль"]')

    @staticmethod
    def check_text_on_page(text):
        return By.XPATH, f'//*[text()="{text}"]'
