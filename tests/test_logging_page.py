
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
        logging_page.check_audit_menu_item()
        assert 'Вы уверены, что хотите включить аудит и хранить историю изменений за выбранный период' in dialog_text,\
            'В модальном окне отсутствует вступительный текст'
        assert 'Все' in dialog_text, 'В модальном окне отсутствует уровень логирования'
        assert 'неделя' in dialog_text, 'В модальном окне отсутствует глубина логирования'
        assert alert_text == 'Аудит успешно запущен', 'Не появился алерт с сообщением'
