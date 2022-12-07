from allure import suite, title

from data.data import UI_ADMIN_USER


@suite('[Pytest][UI]')
class TestAdminPanelAuth:
    """
    Класс для ui-тестов по авторизации и логаута в админ-панели
    """

    @title('Проверка авторизации в админ-панель')
    def test_admin_panel_login(self, admin_login_page, admin_main_page):
        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

    @title('Проверка логаута из админ-панели')
    def test_admin_panel_logout(self, admin_login_page, admin_main_page):
        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_main_page.click_logout_btn()  # клик по кнопке "Logout"
        admin_login_page.assert_open_admin_panel_login_page()  # проверка открытия страницы авторизации
