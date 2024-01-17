from selenium.webdriver.common.by import By


class UserPageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    ADD_LOCAL_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь"]')
    ADD_FREEIPA_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь из Freeipa"]')
    # Поля поиска
    SEARCH_TAB_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    USER_STATUS = (By.XPATH, '//span[contains(@class, "MuiChip-label MuiChip-labelSmall")]')
    # Кебаб меню
    USER_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    USER_FULL_INFO_BUTTON = (By.XPATH, '//span[text()="Полная информация"]')
    FIRED_BUTTON = (By.XPATH, '//span[text()="Уволить"]')
    RESTORE_BUTTON = (By.XPATH, '//span[text()="Восстановить"]')
    # Увольнение пользователя
    CALENDAR_BUTTON = (By.CSS_SELECTOR, 'button[aria-label^="Choose date, selected"]')
    THIS_DAY_PICKER = (By.XPATH,
                       '//button[contains(@class, "MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today")]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(@class, "onboarding__save-button")]')
    # Карточка пользователя
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    USER_CARD_LABEL = (By.XPATH, '//label[contains(@class, "")]')
    USER_CARD_TITLE = (By.XPATH, '//h6[text()="Просмотр полной информации"]')
    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    TAB_CONTACTS = (By.XPATH, '//button[text()="КОНТАКТЫ"]')

    USER_PAGE_TITLE = (By.XPATH, '//h6[text()="Все пользователи"]')
    FILTER_BUTTON = (By.XPATH, '//h6[text()="Отображение"]')
    TAB_FILTER_BUTTONS = (By.XPATH, '//div[@class="ag-floating-filter-button"]/button')

    COLUMNS_HEADERS = (By.CSS_SELECTOR, 'span[ref="eText"]')


