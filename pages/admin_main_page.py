from allure_commons._allure import step

from locators import AdminMainPageLocators as Locators
from pages.base_page import BasePage


class AdminMainPage(BasePage):
    """
    Класс для хранения методов главной странице админ-панели
    """

    path = '/#/admin'

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    def get_available_room_list(self) -> list:
        """
        Получить список доступных для бронирования номеров

        :return: список номеров в формате словаря
        """
        room_list = []
        room_items = self.find_elements(Locators.ROOM_ITEM)
        for room_item in room_items:
            room_number = room_item.find_element(*Locators.ROOM_NUMBER).text
            room_type = room_item.find_element(*Locators.ROOM_TYPE).text
            room_accessibility = room_item.find_element(*Locators.ROOM_ACCESSIBLE).text
            room_price = room_item.find_element(*Locators.ROOM_PRICE).text
            room_details = room_item.find_element(*Locators.ROOM_DETAILS).text.split(', ')
            room_list += [
                {
                    'room_number': room_number,
                    'room_type': room_type,
                    'room_accessibility': room_accessibility,
                    'room_price': room_price,
                    'room_details': room_details,
                }
            ]
        return room_list

    @step('Кликнуть по кнопке "Logout"')
    def click_logout_btn(self):
        """ Клик по кнопке 'Logout' """
        self.find_element(Locators.LOGOUT_BTN).click()

    @step('Ввести значение "{value}" в поле ввода "{field_name}"')
    def enter_value_into_text_field(self, field_name: str, value: str):
        """
        Ввод значения в поле ввода номера комнаты

        :param field_name: наименование поля, в которое вводится значение.
        :param value: вводимое значение.
        """

        if field_name == 'room_number':
            self.fill_edit_field(locator=Locators.ROOM_NUMBER_FIELD, value=value)
        elif field_name == 'room_price':
            self.fill_edit_field(locator=Locators.ROOM_PRICE_FIELD, value=value)
        else:
            raise AssertionError(f'В админке отсутствует поле ввода "{field_name}"')

    @step('Выбрать значение "{value}" в выпадающем списке "{field_name}"')
    def select_value_in_dropdown(self, field_name: str, value: str):
        """
        Выбор значения в выпадающем списке

        :param field_name: наименование поля, в котором выбирается значение.
        :param value: выбираемое значение.
        """

        if field_name == 'room_type':
            self.click_select_by_text(locator=Locators.ROOM_TYPE_FIELD, value=value)
        elif field_name == 'room_accessibility':
            self.click_select_by_text(locator=Locators.ROOM_ACCESSIBLE_FIELD, value=value)
        else:
            raise AssertionError(f'В админке отсутствует выпадающий список "{field_name}"')

    @step('Кликнуть по чекбоксу "{checkbox_name}"')
    def click_checkbox_by_name(self, checkbox_name: str):
        """
        Клик по чекбоксу с переданным названием

        :param checkbox_name: наименование чекбокса.
        """

        if checkbox_name == 'WiFi':
            self.find_element(Locators.ROOM_DETAILS_WIFI_CHECKBOX).click()
        elif checkbox_name == 'Refreshments':
            self.find_element(Locators.ROOM_DETAILS_REFRESHMENTS_CHECKBOX).click()
        elif checkbox_name == 'TV':
            self.find_element(Locators.ROOM_DETAILS_TV_CHECKBOX).click()
        elif checkbox_name == 'Safe':
            self.find_element(Locators.ROOM_DETAILS_SAFE_CHECKBOX).click()
        elif checkbox_name == 'Radio':
            self.find_element(Locators.ROOM_DETAILS_RADIO_CHECKBOX).click()
        elif checkbox_name == 'Views':
            self.find_element(Locators.ROOM_DETAILS_VIEWS_CHECKBOX).click()
        else:
            raise AssertionError(f'В админке отсутствует чекбокс "{checkbox_name}"')

    @step('Кликнуть по кнопке "Create"')
    def click_create_btn(self):
        """ Клик по кнопке 'Create' """
        self.find_element(Locators.CREATE_BTN).click()

    @step('Кликнуть по иконке удаления комнаты с номером "{room_number}"')
    def click_delete_btn_by_room_number(self, room_number: str):
        """
        Клик по кнопке удаления комнаты

        :param room_number: номер комнаты
        """
        strategy, locator = Locators.ROOM_DELETE_BTN_BY_ROOM_NUMBER
        self.find_element((strategy, locator.format(room_number))).click()

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить авторизацию админом')
    def assert_open_admin_main_page(self):
        """
        Проверка открытия главной страницы админ-панели
        """
        self.find_element(Locators.LOGOUT_BTN)
