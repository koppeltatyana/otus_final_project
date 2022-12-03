from _pytest.fixtures import fixture

from pages import MainPage, AdminMainPage, AdminLoginPage


@fixture(scope='function')
def admin_login_page(browser):
    return AdminLoginPage(browser)


@fixture(scope='function')
def admin_main_page(browser):
    return AdminMainPage(browser)


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)
