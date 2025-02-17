import allure
import pytest
import testit

from endpoints.system_roles_endpoint import SystemRolesEndpoint
from pages.system_role_page import SystemRolePage
from pages.user_page import UserPage


@allure.suite("Системные роли")
class TestSystemRolePage:

    @testit.workItemIds(3503)
    @testit.displayName("7.2.2 Создание системной роли")
    @pytest.mark.smoke
    @allure.title("id-3503 7.2.2 Создание системной роли")
    def test_create_new_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        # Создаем роль
        system_role_page.create_system_role('Контролер')
        system_role_page.press_submit_button()
        # Проверяем роль в дропдауне
        system_role_page.check_role_name_in_dropdown('Контролер')
        # Удаляем роль после теста
        system_role_page.delete_system_role('Контролер')


    @testit.workItemIds(3529)
    @testit.displayName("7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    @pytest.mark.regress
    @allure.title("id-3529 7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    def test_checking_impossibility_deleting_system_role_user(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown('Пользователь')
        system_role_page.check_delete_role_icon_is_disabled()
        assert system_role_page.get_tooltip_text_impossibility_deleting_system_role_user() == \
            'Системную роль "Пользователь" удалить нельзя.', \
            "Отсутствует тултип о невозможности удаления системной роли"
        
    @testit.workItemIds(3504)
    @testit.displayName("7.2.2 (Чек-лист) Проверка ограничений при создании системной роли")
    @pytest.mark.regress
    @allure.title("id-3504 7.2.2 (Чек-лист) Проверка ограничений при создании системной роли")
    def test_checking_restrictions_when_creating_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.press_add_system_role_button()
        # Проверка на обязательные поля
        # system_role_page.check_required_fields() # другая реализация
        # Проверка на обязательность тэгов
        # system_role_page.check_required_tags('Контролер') # другая реализация
        # Проверка на уникальность названия системной роли
        system_role_page.check_uniqueness_system_role_name('Пользователь')
        # Проверка на превышение символов в названии системной роли
        system_role_page.check_char_limit_system_role_name()

    @testit.workItemIds(3520)
    @testit.displayName("7.2.2 Отмена создания системной роли")
    @pytest.mark.regress
    @allure.title("id-3520 7.2.2 Отмена создания системной роли")
    def test_cancel_create_new_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.create_system_role('Контролер')
        system_role_page.press_abort_button()
        system_role_page.check_role_name_not_in_dropdown('Контролер')
    
    @testit.workItemIds(3538)
    @testit.displayName("7.2.6 Создание копии системной роли")
    @pytest.mark.regress
    @allure.title("id-3538 7.2.6 Создание копии системной роли")
    def test_creating_copy_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_roles_endpoint = SystemRolesEndpoint()
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown('Пользователь')
        # Получаем полномочия системной роли Пользователь
        id_role_user = system_roles_endpoint.get_user_system_role_id('Пользователь')
        tags_role_user = system_roles_endpoint.get_tags_system_role_id(id_role_user)
        # Создаем копию системной роли
        role_name_copy = system_role_page.creating_copy_system_role('Пользователь')
        # Получаем полномочия системной роли Копии
        id_role_copy = system_roles_endpoint.get_user_system_role_id(role_name_copy)
        tags_role_copy = system_roles_endpoint.get_tags_system_role_id(id_role_copy)
        assert tags_role_user.sort(key=lambda x: x['id']) == tags_role_copy.sort(key=lambda x: x['id']), \
            'Тэги полномочий системных ролей не совпадают'
        system_role_page.check_role_name_in_dropdown(role_name_copy)
        user_page = UserPage(driver)
        user_page.go_to_user_page_simple()
        user_page.open_system_role_drover()
        assert role_name_copy in user_page.get_all_system_role_names(), \
            'Роли нет в дровере назначения ролей'
        id_role_copy = system_roles_endpoint.get_user_system_role_id(role_name_copy)
        system_roles_endpoint.delete_system_role_id(id_role_copy)

    @testit.workItemIds(3539)
    @testit.displayName("7.2.6 Отмена создания копии системной роли")
    @pytest.mark.regress
    @allure.title("id-3539 7.2.6 Отмена создания копии системной роли")
    def test_cancel_create_copy_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_roles_endpoint = SystemRolesEndpoint()
        # Удаляем роль если есть
        id_role = system_roles_endpoint.get_user_system_role_id('Пользователь_копия')
        if id_role is not None:
            system_roles_endpoint.delete_system_role_id(id_role)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown('Пользователь')
        system_role_page.check_submit_button_is_not_visible()
        system_role_page.press_copy()
        system_role_page.check_modal_window_creating_copy('Пользователь')
        system_role_page.press_abort_button()
        system_role_page.check_role_name_not_in_dropdown('Пользователь_копия')

    @testit.workItemIds(3524)
    @testit.displayName("7.2.4 Удаление системной роли которая единственная присвоенная у пользователя")
    @pytest.mark.smoke
    @allure.title("id-3524 7.2.4 Удаление системной роли которая единственная присвоенная у пользователя")
    def test_deleting_system_role_that_only_one_assigned_to_user(self, login, create_system_role, \
                                                                 create_user_with_one_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_delete_system_role()
        system_role_page.check_modal_window_delete_only_one_system_role(create_system_role['name'], \
                                                                        create_user_with_one_system_role)
        new_system_role = system_role_page.choose_new_system_role_in_dialog()
        system_role_page.press_delete_button_one_system_role()
        system_role_page.check_role_name_not_in_dropdown(create_system_role['name'])
        user_page = UserPage(driver)
        user_page.go_to_user_page_simple()
        user_page.open_system_role_drover()
        all_system_role = user_page.get_all_system_role_names()
        assert create_system_role['name'] not in all_system_role, \
            'Удаленная системная роль есть в дровере назначения ролей'
        assert new_system_role in all_system_role, \
            'Новой назначенной системной роли нет в дровере назначения ролей'

    @testit.workItemIds(3523)
    @testit.displayName("7.2.4 Удаление системной роли которая не присвоена ни одному пользователю")
    @pytest.mark.regress
    @allure.title("id-3523 7.2.4 Удаление системной роли которая не присвоена ни одному пользователю")
    def test_deleting_system_role_that_is_not_assigned_to_user(self, login, create_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_delete_system_role()
        system_role_page.check_modal_window_delete_not_assigned_system_role(create_system_role['name'])
        system_role_page.press_delete_button_one_system_role()
        system_role_page.check_role_name_not_in_dropdown(create_system_role['name'])
        user_page = UserPage(driver)
        user_page.go_to_user_page_simple()
        user_page.open_system_role_drover()
        all_system_role = user_page.get_all_system_role_names()
        assert create_system_role['name'] not in all_system_role, \
            'Удаленная системная роль есть в дровере назначения ролей'

    @testit.workItemIds(3534)
    @testit.displayName("7.2.4 Реакция системы на нажатие кнопки замены не выбрав роль на замену")
    @pytest.mark.regress
    @allure.title("id-3534 7.2.4 Реакция системы на нажатие кнопки замены не выбрав роль на замену")
    def test_system_reaction_press_replace_button_without_select_role(self, login, create_system_role, \
                                                                      create_user_with_one_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_delete_system_role()
        system_role_page.check_modal_window_delete_only_one_system_role(create_system_role['name'], \
                                                                        create_user_with_one_system_role)
        system_role_page.press_delete_button_one_system_role()
        system_role_page.check_modal_window_delete_without_select_role()
        # Удаляем после теста Системную роль
        system_role_page.choose_new_system_role_in_dialog()
        system_role_page.press_delete_button_one_system_role()

    @testit.workItemIds(3526)
    @testit.displayName("7.2.4 Удаление системной роли которая НЕ единственно присвоенная пользователю")
    @pytest.mark.regress
    @allure.title("id-3526 7.2.4 Удаление системной роли которая НЕ единственно присвоенная пользователю")
    def test_deleting_system_role_that_not_only_one_assigned_to_user(self, login, create_system_role, \
                                                                 create_user_with_two_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_delete_system_role()
        system_role_page.check_modal_window_delete_not_assigned_system_role(create_system_role['name'])
        system_role_page.press_delete_button_one_system_role()
        system_role_page.check_role_name_not_in_dropdown(create_system_role['name'])
        user_page = UserPage(driver)
        user_page.go_to_user_page_simple()
        user_page.open_system_role_drover()
        all_system_role = user_page.get_all_system_role_names()
        assert create_system_role['name'] not in all_system_role, \
            'Удаленная системная роль есть в дровере назначения ролей'

    @testit.workItemIds(3527)
    @testit.displayName("7.2.4 Отмена удаления системной роли")
    @pytest.mark.regress
    @allure.title("id-3527 7.2.4 Отмена удаления системной роли")
    def test_cancel_deleting_system_role(self, login, create_system_role, create_user_with_two_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_delete_system_role()
        system_role_page.check_modal_window_delete_not_assigned_system_role(create_system_role['name'])
        system_role_page.press_abort_button()
        system_role_page.check_role_name_in_dropdown(create_system_role['name'])


    @testit.workItemIds(3521)
    @testit.displayName("7.2.3 Редактирование системной роли")
    @pytest.mark.regress
    @allure.title("id-3521 7.2.3 Редактирование системной роли")
    def test_redact_system_role(self, login, create_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_roles_endpoint = SystemRolesEndpoint()
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        # Получаем полномочия системной роли до редактирования
        id_role_user = system_roles_endpoint.get_user_system_role_id(create_system_role['name'])
        tags_role_before = system_roles_endpoint.get_tags_system_role_id(id_role_user)
        system_role_page.press_redact_system_role()
        system_role_page.editing_system_role()
        system_role_page.press_submit_button()
        # Получаем полномочия системной роли после редактирования
        tags_role_after = system_roles_endpoint.get_tags_system_role_id(id_role_user)
        system_role_page.check_role_name_in_dropdown(create_system_role['name'])
        user_page = UserPage(driver)
        user_page.go_to_user_page_simple()
        user_page.open_system_role_drover()
        all_system_role = user_page.get_all_system_role_names()
        assert tags_role_before != tags_role_after, \
            'Изменения внесенные в права не сохранились в системе'
        assert create_system_role['name'] in all_system_role, \
            'Измененной системной роли нет в дровере назначения ролей'

    @testit.workItemIds(3522)
    @testit.displayName("7.2.3 Отмена редактирования системной роли")
    @pytest.mark.regress
    @allure.title("id-3522 7.2.3 Отмена редактирования системной роли")
    def test_cancel_redact_system_role(self, login, create_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_roles_endpoint = SystemRolesEndpoint()
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        # Получаем полномочия системной роли до редактирования
        id_role_user = system_roles_endpoint.get_user_system_role_id(create_system_role['name'])
        tags_role_before = system_roles_endpoint.get_tags_system_role_id(id_role_user)
        system_role_page.press_redact_system_role()
        system_role_page.editing_system_role()
        system_role_page.press_abort_button()
        # Получаем полномочия системной роли после редактирования
        tags_role_after = system_roles_endpoint.get_tags_system_role_id(id_role_user)
        system_role_page.check_role_name_in_dropdown(create_system_role['name'])
        assert tags_role_before == tags_role_after, \
            'Изменения внесенные до отмены сохранения, сохранились в системе'

    @testit.workItemIds(3502)
    @testit.displayName("7.2.2 Реакция системы при выборе чекбоксов C/R/U/D")
    @pytest.mark.regress
    @allure.title("id-3502 7.2.2 Реакция системы при выборе чекбоксов C/R/U/D")
    def test_system_reaction_when_selecting_checkboxes(self, login, create_system_role, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown(create_system_role['name'])
        system_role_page.press_redact_system_role()
        system_role_page.check_system_reaction_when_selecting_checkboxes()
        system_role_page.press_abort_button()

    @testit.workItemIds(3535)
    @testit.displayName("7.2.2 Поиск по тегам в таблице")
    @pytest.mark.regress
    @allure.title("id-3535 7.2.2 Поиск по тегам в таблице")
    def test_search_by_tags_in_table(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.check_search_by_tags('проект')
        # Можно менять иногда
        # system_role_page.check_search_by_tags('таблица')

    @testit.workItemIds(3536)
    @testit.displayName("7.2.2 Реакция системы если тегов соответствующих вводимым значениям не найдено")
    @pytest.mark.regress
    @allure.title("id-3536 7.2.2 Реакция системы если тегов соответствующих вводимым значениям не найдено")
    def test_system_reaction_if_tags_not_found(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.check_system_reaction_if_tags_not_found('блаблабла')
