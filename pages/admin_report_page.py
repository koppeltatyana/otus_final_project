from allure_commons._allure import step
from selenium.webdriver import ActionChains

from locators import AdminReportPageLocators as Locators
from pages.base_page import BasePage


class AdminReportPage(BasePage):
    """
    Класс для хранения методов страницы номера админ-панели
    """

    path = '/#/admin/report'

    # -------------------------------------------------- Действия ---------------------------------------------------- #
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
        action.move_to_element_with_offset(to_element=checkin_btn, xoffset=-10, yoffset=10).click_and_hold().perform()
        action.move_to_element_with_offset(to_element=checkin_btn, xoffset=10, yoffset=10).pause(1).perform()
        action.move_to_element_with_offset(to_element=checkout_btn, xoffset=-10, yoffset=10).pause(1).release()
        action.perform()

    @step('Ввести значение "{value}" в поле ввода "{field_name}"')
    def enter_value_into_field(self, field_name: str, value: str):
        """
        Ввод значения в поле ввода

        :param field_name: наименования поля ввода
        :param value: вводимое значение
        """

        if field_name == 'firstname':
            self.fill_edit_field(locator=Locators.BOOKING_FIRSTNAME_INPUT, value=value)
        elif field_name == 'lastname':
            self.fill_edit_field(locator=Locators.BOOKING_LASTNAME_INPUT, value=value)
        else:
            raise AssertionError(f'На странице нет поля с наименованием "{field_name}"')

    @step('Выбрать значение "{value}" в выпадающем списке "{field_name}"')
    def select_value_in_dropdown(self, field_name: str, value: str):
        """
        Выбор значения в выпадающем списке

        :param field_name: наименование поля, в котором выбирается значение.
        :param value: выбираемое значение.
        """

        if field_name == 'room_number':
            self.click_select_by_text(locator=Locators.BOOKING_ROOM_NUMBER_SELECT, value=value)
        elif field_name == 'deposit_paid':
            self.click_select_by_text(locator=Locators.BOOKING_ROOM_PAID_SELECT, value=value)
        else:
            raise AssertionError(f'В админке отсутствует выпадающий список "{field_name}"')

    @step('Кликнуть по кнопке "Book"')
    def click_book_btn(self):
        self.find_element(Locators.BOOK_BTN).click()

    @step('Кликнуть по кнопке "Cancel"')
    def click_cancel_btn(self):
        self.find_element(Locators.CANCEL_BTN).click()

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить отображения "Календаря" при клике на кнопку "Booking this room"')
    def assert_calendar(self):
        """ Проверка отображения "Календаря" при клике на кнопку "Booking this room" """
        assert self.is_element_present(Locators.CALENDAR_ITEM), 'Элемент календаря не появился на странице'

    @step('Проверить отображение формы для ввода персональных данных при бронировании')
    def assert_booking_window(self):
        self.find_element(Locators.BOOKING_WINDOW_ITEM)
