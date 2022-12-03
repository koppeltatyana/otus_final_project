from allure import suite, title

from data.data import ADMIN_USER


@suite('[Pytest][UI]')
class TestAdminPanelPage:
    """
    Класс для ui-тестов по админ-панели
    """

    @title('Проверка авторизации в админ-панель')
    def test_admin_panel_auth(self, admin_login_page, admin_main_page):
        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку
        admin_login_page.admin_panel_login(
            username=ADMIN_USER['username'],
            password=ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели
