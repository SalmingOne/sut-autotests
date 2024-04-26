from selenium.webdriver.common.by import By


class UserProfilePageLocators:
    # Переход на страницу профиля
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'button[id="profile"]')
    MY_PROFILE_MENU_ITEM = (By.XPATH, '//a[text()="Мой профиль"]')

    PROFILE_TITLE = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle1"]')
    START_WORK = (By.XPATH, '//label[text()="Прием в компанию"]/..//input')
    # Вкладка Образование
    EDUCATION_TAB_BUTTON = (By.XPATH, '//button[text()="Образование"]')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    BREAK_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    ADD_ICON = (By.CSS_SELECTOR, 'button[aria-label="Нажмите, чтобы добавить новую карточку"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    # Вкладка Сертификаты
    CERTIFICATE_TAB_BUTTON = (By.XPATH, '//button[text()="Сертификаты"]')
    # Вкладка Опыт работы
    EXPERIENCES_TAB_BUTTON = (By.XPATH, '//button[text()="Опыт работы"]')
    # Вкладка Резюме
    RESUME_TAB_BUTTON = (By.XPATH, '//button[text()="Резюме"]')
    CREATE_RESUME_BUTTON = (By.XPATH, '//a[text()="Создать"]')
    START_WORK_IN_RESUME = (By.XPATH, '//p[@id="experienceDate"]/..//input')
    READY_TO_WORK_DROPDOWN = (By.CSS_SELECTOR, 'input[role="combobox"]')
    RESUME_TITLE_FIELD = (By.CSS_SELECTOR, 'input[name="title"]')
    RESUME_FULL_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="fullName"]')
    RESUME_POST_FIELD = (By.CSS_SELECTOR, 'input[name="post"]')
    RESUME_DIRECTION_FIELD = (By.CSS_SELECTOR, 'input[name="direction"]')
    EXPERIENCE_PROJECT_NAME = (By.XPATH, '//input[contains(@name,"projectName")]')
    EXPERIENCE_CUSTOMER = (By.XPATH, '//input[contains(@name,"customer")]')
    EXPERIENCE_PROJECT_POST = (By.XPATH, '//input[contains(@name,"projectPost")]')
    ADD_EXPERIENCE_BUTTON = (By.XPATH, '//button[text()="Добавить"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    DATE_PIKERS = (By.CSS_SELECTOR, 'input[type="tel"]')
    WYSIWYG_TITLES = (By.XPATH, '//div[contains(@class,"MuiPaper-rounded MuiPaper-elevation0")]//div[@id]/*[contains(@class, "MuiTypography")]')
    WYSIWYG_INCLUDES_FUNCTION_TITLES = (By.XPATH, '//div[@id="workStack"]//div[@style="visibility: visible;"]//*[@title]')
    CURRENT_EMPLOYER_CHECKBOX = (By.XPATH, '//span[text()="Текущий работодатель"]')

    RESUME_TITLES_ON_TAB = (By.CSS_SELECTOR, 'div[col-id="title"][role="gridcell"]')
    SEARCH_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')

    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')

    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBABS_DEL_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    KEBAB_MENU_ITEM = (By.XPATH, '//li//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
