from _pytest.fixtures import fixture

from pages import MainPage


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)
