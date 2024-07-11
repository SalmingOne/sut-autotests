from selenium.webdriver.common.by import By


class UserProfilePageLocators:
    # Переход на страницу профиля
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'button[id="profile"]')
    MY_PROFILE_MENU_ITEM = (By.XPATH, '//a[text()="Мой профиль"]')
    MY_PROFILE_TAB_BUTTON = (By.XPATH, '//div[text()="Информация о сотруднике"]/..')
    PROFILE_TITLE = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle1"]')
    START_WORK = (By.XPATH, '//label[text()="Прием в компанию"]/..//input')
    CHILDREN_TEXT_AREA = (By.CSS_SELECTOR, 'textarea[name="children"]')
    FAMILY_STATUS = (By.XPATH, '//div[@name="maritalStatus"]//input')
    NOT_SELECTED_LI = (By.CSS_SELECTOR, 'li[role="option"][aria-selected="false"]')
    BORN_DATE = (By.XPATH, '//label[text()="Дата рождения"]/..//input')
    EMAIL_TEXT_AREA = (By.CSS_SELECTOR, 'textarea[name="email"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    PHONE_TEXT_AREA = (By.CSS_SELECTOR, 'textarea[name="phone"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[name="phone"]')
    # Модальное окно с диалогом
    ALERT_DIALOG_DESCRIPTION = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')

    CANSEL_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]/..//button[text()="Отменить"]')
    # Вкладка Образование
    EDUCATION_TAB_BUTTON = (By.XPATH, '//div[text()="Образование"]/..')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    BREAK_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    ADD_ICON = (By.CSS_SELECTOR, 'button[aria-label="Нажмите, чтобы добавить новую карточку"]')
    CHECK_DIPLOMA_TITLE = (By.XPATH, '//h6[text()="Диплом"]')
    EDUCATION_FORM = (By.CSS_SELECTOR, 'input[placeholder="Выберите форму обучения"]')
    EDUCATION_LEVEL = (By.CSS_SELECTOR, 'input[placeholder="Выберите уровень"]')
    FACULTY = (By.CSS_SELECTOR, 'input[placeholder="Введите факультет"]')
    DIRECTION = (By.CSS_SELECTOR, 'input[placeholder="Выберите направление"]')
    INSTITUTION_NAME = (By.CSS_SELECTOR, 'input[placeholder="Введите название"]')
    FACULTY_NAME = (By.CSS_SELECTOR, 'input[placeholder="Введите факультет"]')
    SPECIALIZATION_NAME = (By.CSS_SELECTOR, 'input[placeholder="Введите специальность"]')
    YEAR_OF_GRADUATION = (By.CSS_SELECTOR, 'input[placeholder="Введите год окончания"]')
    DELETE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')
    FILE_INPUT = (By.XPATH, '//div[@aria-label="Приложите файлы. Допустимый формат: PDF, DOCX, PNG, JPEG, JPG. Суммарный размер: <=5Мб"]//input[@type="file"]')
    FILE_INPUT_CHECK = (By.XPATH, '//div[@aria-label="Приложите файлы. Допустимый формат: PDF, DOCX, PNG, JPEG, JPG. Суммарный размер: <=5Мб"]//label')
    FILE_DOWNLOAD_ICON = (By.CSS_SELECTOR, 'svg[data-testid="FileDownloadIcon"]')

    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    # Вкладка Сертификаты
    CERTIFICATE_TAB_BUTTON = (By.XPATH, '//div[text()="Сертификаты"]/..')
    CERTIFICATE_NAME = (By.CSS_SELECTOR, 'input[placeholder="Введите название"]')
    CERTIFICATE_DATA_PICKER = (By.CSS_SELECTOR, 'svg[data-testid="CalendarTodayOutlinedIcon"]')
    DAY_AFTER_THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]//following::button[1]')
    CERTIFICATE_TITLE = (By.XPATH, '//a[contains(@class,"MuiTypography-root MuiTypography-body2 MuiLink-root MuiLink-underlineHover")]//h6')
    # Вкладка Опыт работы
    EXPERIENCES_TAB_BUTTON = (By.XPATH, '//div[text()="Опыт работы"]/..')
    EXPERIENCES_EMPLOYER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите работодателя"]')
    EXPERIENCES_PROJECT_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите проект"]')
    EXPERIENCES_CUSTOM_PROJECT_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Введите проект"]')
    EXPERIENCES_SPECIALIZATION_ACTION = (By.CSS_SELECTOR, 'input[placeholder="Выберите деятельность"]')
    EXPERIENCES_SPECIALIZATION_SLOT = (By.CSS_SELECTOR, 'input[placeholder="Выберите роль"]')
    EXPERIENCES_DESCRIPTION = (By.CSS_SELECTOR, 'div[aria-label="rdw-wrapper"]')
    EXPERIENCES_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'span[data-text]')

    EXPERIENCES_DATA_PICKER = (By.CSS_SELECTOR, 'button[aria-label="Choose date"]')
    NEXT_DAY_IN_PICKER = (By.XPATH, '//button[contains(@class, "today")]//following::button[1]')
    EXPERIENCES_TITLE = (By.XPATH, '//div[contains(@name,"employer")]')
    EXPERIENCES_BEGIN_DATA_INPUT = (By.XPATH, '//label[text()="Дата начала работы"]/..//input')
    EXPERIENCES_KNOWLEDGE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите уровни"]')
    # Вкладка Резюме
    RESUME_TAB_BUTTON = (By.XPATH, '//div[text()="Резюме"]/..')
    CREATE_RESUME_BUTTON = (By.XPATH, '//a[text()="Создать"]')
    START_WORK_IN_RESUME = (By.XPATH, '//p[@id="experienceDate"]/..//input')
    READY_TO_WORK_DROPDOWN = (By.CSS_SELECTOR, 'input[role="combobox"]')
    RESUME_TITLE_FIELD = (By.CSS_SELECTOR, 'input[name="title"]')
    RESUME_FULL_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="fullName"]')
    RESUME_POST_FIELD = (By.CSS_SELECTOR, 'input[name="post"]')
    RESUME_DIRECTION_FIELD = (By.CSS_SELECTOR, 'input[name="direction"]')
    EXPERIENCE_PROJECT_NAME = (By.XPATH, '//input[contains(@name,"projectName")]')
    RESUME_EXPERIENCE_START_DATE = (By.XPATH, '//p[text()="Начало работы"]/..//input')
    RESUME_EXPERIENCE_END_DATE = (By.XPATH, '//p[text()="Окончание работы"]/..//input')
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
    BREAK_IN_MODAL = (By.XPATH, '//div[@aria-label="Выйти без сохранения"]//button[text()="Отменить"]')

    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')

    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBABS_DEL_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    KEBAB_MENU_ITEM = (By.XPATH, '//li//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def check_text(self, text):
        return (By.XPATH, f'//*[text()="{text}"]')