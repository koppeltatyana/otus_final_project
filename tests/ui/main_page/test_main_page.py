import datetime
from random import randint

from allure import suite, title

from utils.helpers import random_user_data


@suite('[Pytest][UI]')
class TestMainPage:
    """
    Класс для ui-тестов главной страницы сайта
    """

    @title('Проверить отображение карты на главной странице сайта')
    def test_map_main_page(self, main_page):
        main_page._open()
        main_page.close_welcome_msg()
        main_page.assert_open_main_page()
        main_page.assert_map_on_the_main_page()

    @title('Бронирование номера с главной страницы сайта')
    def test_user_booking(self, main_page, add_room, delete_room_after_test):
        # тестовые данные
        room_info = add_room(room_availability=True)  # создание нового номера без бронирований
        user_data = random_user_data()  # получение данных пользователя
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 2))).day  # дата заезда
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(3, 9))).day  # дата выезда

        # --------------------------- Сохранение номера комнаты, чтобы потом его удалить ----------------------------- #
        delete_room_after_test(room_number=room_info['room_number'])
        # ------------------------------------------------------------------------------------------------------------ #

        main_page._open()
        main_page.close_welcome_msg()
        main_page.assert_open_main_page()

        ui_room_list = main_page.get_main_page_room_list()  # получить список номеров с главной странице
        room_index = len(ui_room_list) - 1  # получить индекс бронируемого номера

        main_page.click_booking_btn_by_index(room_index=room_index)  # кликнуть по кнопке "Booking this room"
        main_page.assert_calendar()  # проверить появление календаря на странице для выбора дат бронирования

        main_page.choose_calendar_dates(checkin=checkin, checkout=checkout)  # выбор дат бронирования

        # заполнение персональных данных
        main_page.enter_value_into_field(field_name='firstname', value=user_data['firstname'])
        main_page.enter_value_into_field(field_name='lastname', value=user_data['lastname'])
        main_page.enter_value_into_field(field_name='email', value=user_data['email'])
        main_page.enter_value_into_field(field_name='phone', value=user_data['phone'])
        main_page.click_book_btn()  # клик по кнопке "Book"

        main_page.assert_booking_successful_modal_window()
        main_page.click_close_successful_modal_window()  # закрыть модальное окно после успешного бронирования

    @title('Невозможность бронирования на недоступные даты')
    def test_impossible_booking(self, main_page, add_main_page_booking, delete_room_after_test):
        # тестовые данные
        room_info, user_booking_info = add_main_page_booking

        user_data = random_user_data()  # получение данных пользователя
        checkin = (datetime.datetime.today() + datetime.timedelta(days=7)).day  # дата заезда
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(8, 9))).day  # дата выезда
        user_data['checkin'] = checkin
        user_data['checkout'] = checkout

        # --------------------------- Сохранение номера комнаты, чтобы потом его удалить ----------------------------- #
        delete_room_after_test(room_number=room_info['room_number'])
        # ------------------------------------------------------------------------------------------------------------ #

        main_page._open()
        main_page.close_welcome_msg()
        main_page.assert_open_main_page()

        ui_room_list = main_page.get_main_page_room_list()  # получить список номеров с главной странице
        room_index = len(ui_room_list) - 1  # получить индекс бронируемого номера

        main_page.click_booking_btn_by_index(room_index=room_index)  # кликнуть по кнопке "Booking this room"
        main_page.assert_calendar()  # проверить появление календаря на странице для выбора дат бронирования

        main_page.choose_calendar_dates(
            checkin=user_booking_info['checkin'],
            checkout=user_booking_info['checkout'],
        )  # выбор дат бронирования

        # заполнение персональных данных
        main_page.enter_value_into_field(field_name='firstname', value=user_data['firstname'])
        main_page.enter_value_into_field(field_name='lastname', value=user_data['lastname'])
        main_page.enter_value_into_field(field_name='email', value=user_data['email'])
        main_page.enter_value_into_field(field_name='phone', value=user_data['phone'])
        main_page.click_book_btn()  # клик по кнопке "Book"

        main_page.assert_error_msg()  # проверить отображение сообщения с ошибкой
