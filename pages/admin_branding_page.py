from time import sleep

from allure_commons._allure import step
from selenium.webdriver import Keys

from locators import AdminBrandingPageLocators as Locators
from pages.base_page import BasePage


class AdminBrandingPage(BasePage):
    """
    Класс для хранения методов страницы номера админ-панели
    """

    path = '/#/admin/branding'

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    @step('Ввести значение "{value}" в поле ввода "{field_name}"')
    def enter_value_into_field_name(self, field_name: str, value: str):
        """
        Ввод значения в поле ввода

        :param field_name: наименование поля ввода
        :param value: вводимое значение
        """
        if field_name == 'description':
            _input = self.find_element(Locators.DESC_INPUT)
            _input.click()
            sleep(0.5)
            _input.send_keys(Keys.CONTROL, 'a')
            sleep(0.5)
            _input.send_keys(Keys.DELETE)
            sleep(0.5)
            _input.send_keys(value)
        elif field_name == 'contact_name':
            _input = self.find_element(Locators.CONTACT_NAME_INPUT)
            _input.click()
            sleep(0.5)
            _input.send_keys(Keys.CONTROL, 'a')
            sleep(0.5)
            _input.send_keys(Keys.DELETE)
            sleep(0.5)
            _input.send_keys(value)
        elif field_name == 'contact_address':
            _input = self.find_element(Locators.CONTACT_ADDRESS_INPUT)
            _input.click()
            sleep(0.5)
            _input.send_keys(Keys.CONTROL, 'a')
            sleep(0.5)
            _input.send_keys(Keys.DELETE)
            sleep(0.5)
            _input.send_keys(value)
        elif field_name == 'contact_phone':
            _input = self.find_element(Locators.CONTACT_PHONE_INPUT)
            _input.click()
            sleep(0.5)
            _input.send_keys(Keys.CONTROL, 'a')
            sleep(0.5)
            _input.send_keys(Keys.DELETE)
            sleep(0.5)
            _input.send_keys(value)
        elif field_name == 'contact_email':
            _input = self.find_element(Locators.CONTACT_EMAIL_INPUT)
            _input.click()
            sleep(0.5)
            _input.send_keys(Keys.CONTROL, 'a')
            sleep(0.5)
            _input.send_keys(Keys.DELETE)
            sleep(0.5)
            _input.send_keys(value)
        else:
            raise AssertionError(f'На странице нет поля ввода "{field_name}"')

    @step('Кликнуть по кнопке "Submit"')
    def click_submit_btn(self):
        self.find_element(Locators.SUBMIT_BTN).click()
        sleep(1)

    @step('Кликнуть по кнопке "Close" в алерте')
    def click_close_alert_btn(self):
        self.find_element(Locators.CLOSE_BTN).click()
        sleep(1)

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить открытие страницы "Branding"')
    def assert_open_branding_page(self):
        self.find_element(Locators.TITLE), 'Страница "Branding" не была открыта'
