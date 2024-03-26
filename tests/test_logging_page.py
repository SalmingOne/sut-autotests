
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
