from allure_commons._allure import step

from locators import AdminLoginPageLocators as Locators
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    """
    Класс для хранения методов страницы авторизации в админ-панель
    """
    path = '/#/admin'

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    def close_welcome_msg(self):
        self.find_element(Locators.LET_ME_HACK_BTN).click()

    def enter_value_into_login_field(self, value: str):
        """
        Ввод значения в поле ввода "Username"

        :param value: значение, которое необходимо ввести в поле ввода
        """
        self.fill_edit_field(locator=Locators.LOGIN_INPUT, value=value)

    def enter_value_into_password_field(self, value: str):
        """
        Ввод значения в поле ввода "Password"

        :param value: значение, которое необходимо ввести в поле ввода
        """
        self.fill_edit_field(locator=Locators.PASSWORD_INPUT, value=value)

    def click_login_btn(self):
        """
        Клик по кнопке "Login"
        """
        self.find_element(Locators.LOGIN_BTN).click()

    @step('Авторизоваться в админ панели с логином {username} и паролем {password}')
    def admin_panel_login(self, username: str, password: str):
        """
        Авторизация в админ-панели

        :param username: имя пользователя
        :param password: пароль пользователя
        """
        self.enter_value_into_login_field(value=username)
        self.enter_value_into_password_field(value=password)
        self.click_login_btn()

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить открытие страницы авторизации в админ-панель')
    def assert_open_admin_panel_login_page(self):
        """
        Проверка открытия страницы авторизации в админ-панель
        """
        self.is_element_visible(Locators.PAGE_TITLE, timeout=10)
