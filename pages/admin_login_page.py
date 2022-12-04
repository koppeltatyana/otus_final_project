from allure_commons._allure import step

from locators import AdminLoginPageLocators as Locators
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    """
    Класс для хранения методов страницы авторизации в админ-панель
    """
    path = '/#/admin'

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    @step('Закрыть приветственное сообщение при существовании такового')
    def close_welcome_msg(self):
        if self.is_element_present(Locators.LET_ME_HACK_BTN):
            self.find_element(Locators.LET_ME_HACK_BTN).click()

    @step('Ввести значение в поле ввода "Username"')
    def enter_value_into_login_field(self, value: str):
        """
        Ввод значения в поле ввода "Username"

        :param value: значение, которое необходимо ввести в поле ввода
        """
        self.fill_edit_field(locator=Locators.LOGIN_INPUT, value=value)

    @step('Ввести значение в поле ввода "Password"')
    def enter_value_into_password_field(self, value: str):
        """
        Ввод значения в поле ввода "Password"

        :param value: значение, которое необходимо ввести в поле ввода
        """
        self.fill_edit_field(locator=Locators.PASSWORD_INPUT, value=value)

    @step('Кликнуть по кнопке "Login"')
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
        if self.is_element_present(Locators.PAGE_TITLE, timeout=10):
            self.enter_value_into_login_field(value=username)
            self.enter_value_into_password_field(value=password)
            self.click_login_btn()

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить открытие страницы авторизации в админ-панель')
    def assert_open_admin_panel_login_page(self):
        """
        Проверка открытия страницы авторизации в админ-панель
        """
        assert self.is_element_present(Locators.PAGE_TITLE, timeout=10)
