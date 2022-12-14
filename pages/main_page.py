from allure_commons._allure import step
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from locators import MainPageLocators as Locators


class MainPage(BasePage):
    """
    Класс для хранения методов главной страницы
    """

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    def get_main_page_room_list(self):
        """
        Получить список номеров с главной страницы

        :return: список номеров и их описаний
        """
        room_list = []
        room_items = self.find_elements(Locators.ROOM_ITEM)
        for item in room_items:
            room_list += [
                {
                    'room_type': item.find_element(*Locators.ROOM_TYPE).text,
                    'room_description': item.find_element(*Locators.ROOM_DESCRIPTION).text,
                    'room_details': [x.text for x in item.find_elements(*Locators.ROOM_DETAILS)]
                }
            ]
        return room_list

    @step('Кликнуть по кнопке "Book this room"')
    def click_booking_btn_by_index(self, room_index: int):
        """
        Клик по кнопке "Book this room"

        :param room_index: номер комнаты по порядку (начиная с 0)
        """
        room_list = self.get_main_page_room_list()
        if room_index > len(room_list) or room_index < 0:
            raise AssertionError('Вы выбрали индекс несуществующего номера')
        booking_btns = self.find_elements(Locators.BOOKING_BTN)
        booking_btns[room_index].click()

    @step('Кликнуть по кнопке "Book" при бронировании')
    def click_book_btn(self):
        """ Клик по кнопке 'Book' при бронировании """
        self.find_element(Locators.BOOK_BTN).click()

    @step('Выбрать даты пребывания (с {checkin} по {checkout}')
    def choose_calendar_dates(self, checkin: int, checkout: int):
        """
        Выбор дат пребывания

        :param checkin: дата заезда
        :param checkout: дата выезда
        """
        if checkin < 1 or checkout < 1:
            raise AssertionError('Выберите корректные даты')

        self.hover(locator=Locators.CALENDAR_ITEM)
        checkin = str(checkin) if checkin > 9 else '0' + str(checkin)
        checkout = str(checkout) if checkout > 9 else '0' + str(checkout)
        print(checkin, checkout)
        strategy, locator = Locators.CALENDAR_DAY_BTN
        checkin_btn = self.find_element((strategy, locator.format(checkin)))
        checkout_btn = self.find_element((strategy, locator.format(checkout)))

        action = ActionChains(self.driver)
        action.move_to_element_with_offset(to_element=checkin_btn, xoffset=-10, yoffset=10).click_and_hold()
        action.move_to_element_with_offset(to_element=checkin_btn, xoffset=10, yoffset=10).pause(1)
        action.move_to_element_with_offset(to_element=checkout_btn, xoffset=-10, yoffset=10).pause(1).release()
        action.perform()

    @step('Ввести значение {value} в поле ввода {field_name}')
    def enter_value_into_field(self, field_name: str, value: str):
        """
        Ввод значения в поле ввода

        :param field_name: наименование поля ввода (firstname, lastname, email, phone)
        :param value: вводимое значение
        """
        if field_name == 'firstname':
            self.fill_edit_field(locator=Locators.BOOKING_FIRSTNAME_INPUT, value=value)
        elif field_name == 'lastname':
            self.fill_edit_field(locator=Locators.BOOKING_LASTNAME_INPUT, value=value)
        elif field_name == 'email':
            self.fill_edit_field(locator=Locators.BOOKING_EMAIL_INPUT, value=value)
        elif field_name == 'phone':
            self.fill_edit_field(locator=Locators.BOOKING_PHONE_INPUT, value=value)
        else:
            raise AssertionError(f'Поля "{field_name}" нет среди полей при бронировании')

    @step('Кликнуть по кнопке "Close" в модальном окне после успешного бронирования')
    def click_close_successful_modal_window(self):
        self.find_element(Locators.CLOSE_SUCCESSFUL_MODAL_WINDOW_BTN).click()

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить заголовок "Rooms" на странице')
    def assert_open_main_page(self):
        """ Проверка отображения заголовка "Rooms" на главной странице """
        assert self.is_element_present(Locators.TITLE), 'Главная страница не была открыта'

    @step('Проверить контактную информацию на сайте')
    def assert_contact_info(
        self, expected_name: str = None, expected_address: str = None, expected_phone: str = None,
        expected_email: str = None,
    ):
        if expected_name is not None:
            actual_name = self.find_element(Locators.CONTACT_NAME).text
            assert actual_name == expected_name, \
                f'Контактное имя не соответствует ожидаемому. ОР: {expected_name}. ОР: {actual_name}'
        if expected_address is not None:
            actual_address = self.find_element(Locators.CONTACT_ADDRESS).text
            assert actual_address == expected_address, \
                f'Контактный адрес не соответствует ожидаемому. ОР: {expected_address}. ОР: {actual_address}'
        if expected_phone is not None:
            actual_phone = self.find_element(Locators.CONTACT_PHONE).text
            assert actual_phone == expected_phone, \
                f'Контактный номер телефона не соответствует ожидаемому. ОР: {expected_phone}. ОР: {actual_phone}'
        if expected_email is not None:
            actual_email = self.find_element(Locators.CONTACT_EMAIL).text
            assert actual_email == expected_email, \
                    f'Контактная эл. почта не соответствует ожидаемому. ОР: {expected_email}. ОР: {actual_email}'

    @step('Проверить соответствие фактического описания и ожидаемого')
    def assert_site_description(self, expected_desc: str):
        """ Проверка соответствия фактического описания и ожидаемого """
        actual_desc = self.find_element(Locators.DESCRIPTION).text
        assert actual_desc == expected_desc, 'Актуальное описание не соответствует ожидаемому. ' \
                                             f'ОР: {expected_desc}. ФР: {actual_desc}'

    @step('Проверить отображение сообщения об ошибки')
    def assert_error_msg(self):
        """
        Проверка отображения сообщения 'The room dates are either invalid or are already booked for
        one or more of the dates that you have selected.'
        """
        exp_res = 'The room dates are either invalid or are already booked for one or more of the dates that you ' \
                  'have selected.'
        msg = self.find_element(Locators.ERROR_MSG).text
        assert msg == exp_res, f'Сообщение об ошибке не соответствует ожидаемому. ОР: "{exp_res}". ФР: "{msg}"'

    @step('Проверить отображения "Календаря" при клике на кнопку "Booking this room"')
    def assert_calendar(self):
        """ Проверка отображения "Календаря" при клике на кнопку "Booking this room" """
        assert self.is_element_present(Locators.CALENDAR_ITEM), 'Элемент календаря не появился на странице'

    @step('Проверить отображение модального окна "Booking Successful!" после успешного бронирования')
    def assert_booking_successful_modal_window(self):
        assert self.is_element_present(Locators.BOOKING_SUCCESSFUL_MODAL_WINDOW_TITLE), \
            'Бронирование номера не было произведено'

    @step('Проверить отображение карты на главной странице сайта')
    def assert_map_on_the_main_page(self):
        """ Проверка отображения карты на главной странице сайта """
        assert self.is_element_present(Locators.MAP), 'На главной странице сайта нет карты'
