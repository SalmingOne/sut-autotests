import time

import allure
import pytest
import testit

from pages.logging_page import LoggingPage


@allure.suite("Страница логирования")
class TestLoggingPage:
    @testit.workItemIds(1411)
    @testit.displayName("6.4.3 Включение логирования")
    @pytest.mark.smoke
    @allure.title("id-1411 6.4.3 Включение логирования")
    def test_enabling_logging(self, logging_off, login, driver):
        logging_page = LoggingPage(driver)
        logging_page.go_to_audit_page()
        logging_page.change_audit_setting(status='Вкл', level='Все', depth='Неделя')
        dialog_text = logging_page.get_modal_window()
        logging_page.check_modal_abort_button()
        logging_page.submit_modal_dialog()
        alert_text = logging_page.get_alert_text()
        audit_on_menu = logging_page.check_audit_menu_item()
        assert 'Вы уверены, что хотите включить аудит и хранить историю изменений за выбранный период' in dialog_text,\
            'В модальном окне отсутствует вступительный текст'
        assert 'Все' in dialog_text, 'В модальном окне отсутствует уровень логирования'
        assert 'неделя' in dialog_text, 'В модальном окне отсутствует глубина логирования'
        assert alert_text == 'Аудит успешно запущен', 'Не появился алерт с сообщением'
        assert audit_on_menu, 'Нет пункта меню Аудит'

    @testit.workItemIds(1231)
    @testit.displayName("6.4.3 Выключение логирования")
    @pytest.mark.smoke
    @allure.title("id-1231 6.4.3 Выключение логирования")
    def test_disabling_logging(self, logging_on, login, driver):
        logging_page = LoggingPage(driver)
        logging_page.go_to_audit_page()
        logging_page.disabling_logging()
        dialog_text = logging_page.get_modal_window()
        logging_page.submit_modal_dialog()
        alert_text = logging_page.get_alert_text()
        audit_on_menu = logging_page.check_audit_menu_item()
        assert dialog_text == 'Вы уверены, что хотите отключить аудит?', 'Не корректный текст в модальном окне'
        assert alert_text == 'Аудит отключен', 'Не появилось сообщение об отключении аудита'
        assert not audit_on_menu, 'Нет скрылся пункт меню Аудит'

    @testit.workItemIds(1228)
    @testit.displayName('6.4.3 Содержание таба "Аудит"')
    @pytest.mark.regress
    @allure.title('id-1228 6.4.3 Содержание таба "Аудит"')
    def test_view_tab_audit(self, logging_on, login, driver):
        logging_page = LoggingPage(driver)
        logging_page.go_to_audit_page()
        logging_page.check_elements_on_page()
        logging_page.check_elements_in_select()
        logging_page.buttons_are_disabled()

    @testit.workItemIds(1230)
    @testit.displayName('6.4.3 Реакция системы при выборе значения "Вкл"')
    @pytest.mark.regress
    @allure.title('id-1230 6.4.3 Реакция системы при выборе значения "Вкл"')
    def test_system_reaction_when_on_is_selected(self, logging_off, login, driver):
        logging_page = LoggingPage(driver)
        logging_page.go_to_audit_page()
        logging_page.change_audit_status(status='Вкл')
        logging_page.fields_are_enabled()
        logging_page.buttons_are_enabled()

    @testit.workItemIds(1412)
    @testit.displayName('6.4.3 Отмена включения логирования')
    @pytest.mark.regress
    @allure.title('id-1412 6.4.3 Отмена включения логирования')
    def test_cancel_enable_logging(self, logging_off, login, driver):
        logging_page = LoggingPage(driver)
        logging_page.go_to_audit_page()
        logging_page.change_audit_setting(status='Вкл', level='Все', depth='Неделя')
        logging_page.discard_audit_setting_changes()
        values = logging_page.get_field_values()
        assert values[0] == 'Вкл', 'Поле статус аудита не содержит введённое ранее значение'
        assert values[1] == 'Все', 'Поле уровень аудита не содержит введённое ранее значение'
        assert values[2] == '1', 'Поле количество не содержит введённое ранее значение'
        assert values[3] == 'Неделя', 'Поле глубина аудита не содержит введённое ранее значение'
