from allure_commons._allure import step

from locators import AdminRoomDetailsPageLocators as Locators
from pages.base_page import BasePage


class AdminRoomDetailsPage(BasePage):
    """
    Класс для хранения методов страницы номера админ-панели
    """

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    @step('Кликнуть кнопку "Edit"')
    def click_edit_btn(self):
        """ Клик по кнопке 'Edit' """
        self.find_element(Locators.EDIT_BTN).click()

    @step('Кликнуть кнопку "Update"')
    def click_update_btn(self):
        """ Клик по кнопке 'Update' """
        self.find_element(Locators.UPDATE_BTN).click()

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
        elif field_name == 'room_description':
            self.fill_edit_field(locator=Locators.ROOM_DESC_FIELD, value=value)
        elif field_name == 'room_image':
            self.fill_edit_field(locator=Locators.ROOM_IMG_FIELD, value=value)
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

    def get_reservation_list(self):
        """
        Получение списка бронирований

        :return: список бронироний
        """
        room_id = int(self.driver.current_url.split('/')[-1])
        booking_list = []
        try:
            strategy, locator = Locators.BOOKING_ITEM
            booking_items = self.find_elements((strategy, locator.format(room_id)))
        except Exception:
            return []

        for booking in booking_items:
            firstname = booking.find_element(*Locators.BOOKING_FIRSTNAME).text
            lastname = booking.find_element(*Locators.BOOKING_LASTNAME).text
            price = booking.find_element(*Locators.BOOKING_PRICE).text
            is_paid = booking.find_element(*Locators.BOOKING_DEPOSIT_PAID).text
            checkin = booking.find_element(*Locators.BOOKING_CHECKIN).text
            checkout = booking.find_element(*Locators.BOOKING_CHECKOUT).text
            booking_list += [
                {
                    'firstname': firstname,
                    'lastname': lastname,
                    'price': int(price),
                    'deposit_paid': is_paid,
                    'checkin': checkin,
                    'checkout': checkout,
                }
            ]
        return booking_list

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить открытие страницы деталей номера "{room_number}"')
    def assert_open_room_details_page(self, room_number: str):
        """
        Проверка открытия нужной страницы деталей номера

        :param room_number: номер комнаты
        """
        strategy, locator = Locators.PAGE_TITLE_BY_ROOM_NUMBER
        assert self.is_element_present((strategy, locator.format(room_number))), \
            f'Страница деталей номера "{room_number}" не была открыта'
