import allure

from pages.colleagues_page import ColleaguesPage


@allure.suite("Пользователи")
class TestUsersPage:

    @allure.title("id-981 4.9.1. Просмотр страницы коллег пользователя в разделе Коллеги")
    def test_view_colleagues_page(self, login, driver):
        colleagues_page = ColleaguesPage(driver)
        colleagues_page.go_colleagues_page()
        colleagues_page.check_colleagues_title()
        colleagues_page.check_colleagues_page_tabs()
        colleagues_page.check_search_field()
        colleagues_page.check_to_advanced_search_button()
        colleagues_page.check_subtitle()
        colleagues_page.check_setting_icon()
        colleagues_page.check_column_titles()
        colleagues_page.check_user_name_link()



    #Таблицу с возможностью перехода на страницу профиля пользователя со столбцами по умолчанию:

