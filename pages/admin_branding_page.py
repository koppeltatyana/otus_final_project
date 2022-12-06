from time import sleep

from allure_commons._allure import step
from selenium.webdriver import ActionChains

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
            action = ActionChains(self.driver)
            action.click(on_element=self.find_element(Locators.DESC_INPUT)).pause(1).\
                double_click().pause(1).send_keys(value).pause(1).perform()
        elif field_name == 'contact_name':
            self.fill_edit_field(locator=Locators.CONTACT_NAME_INPUT, value=value)
        elif field_name == 'contact_address':
            self.fill_edit_field(locator=Locators.CONTACT_ADDRESS_INPUT, value=value)
        elif field_name == 'contact_phone':
            self.fill_edit_field(locator=Locators.CONTACT_PHONE_INPUT, value=value)
        elif field_name == 'contact_email':
            self.fill_edit_field(locator=Locators.CONTACT_EMAIL_INPUT, value=value)
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
