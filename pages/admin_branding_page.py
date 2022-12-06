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
        action = ActionChains(self.driver)
        if field_name == 'description':
            action.click(on_element=self.find_element(Locators.DESC_INPUT)).pause(1).\
                double_click().double_click().pause(0.5).send_keys(value).pause(1).perform()
        elif field_name == 'contact_name':
            action.click(on_element=self.find_element(Locators.CONTACT_NAME_INPUT)).pause(0.5). \
                double_click().double_click().pause(0.5).send_keys(value).pause(0.5).perform()
        elif field_name == 'contact_address':
            action.click(on_element=self.find_element(Locators.CONTACT_ADDRESS_INPUT)).pause(0.5). \
                double_click().double_click().pause(0.5).send_keys(value).pause(0.5).perform()
        elif field_name == 'contact_phone':
            action.click(on_element=self.find_element(Locators.CONTACT_PHONE_INPUT)).pause(0.5). \
                double_click().double_click().pause(0.5).send_keys(value).pause(0.5).perform()
        elif field_name == 'contact_email':
            action.click(on_element=self.find_element(Locators.CONTACT_EMAIL_INPUT)).pause(0.5). \
                double_click().double_click().pause(0.5).send_keys(value).pause(0.5).perform()
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
