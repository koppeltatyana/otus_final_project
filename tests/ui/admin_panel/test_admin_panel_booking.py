import datetime
from random import randint, choice
from time import sleep

import pytest
from allure import suite, title

from data.data import UI_ADMIN_USER
from utils.helpers import random_user_data


@suite('[Pytest][UI]')
class TestAdminPanelBooking:
    """
    Класс для ui-тестов бронирования в админ панели
    """

    @title('Бронирование через админ-панель')
    @pytest.mark.xfail(reason='Неверно проставляется дата выезда')
    @pytest.mark.no_parallel
    def test_admin_panel_booking(
        self, add_room, admin_main_page, admin_login_page, admin_report_page, admin_room_details_page,
    ):

        # подготовка тестовых данных
        room_info = add_room(room_availability=True)
        user_data = random_user_data()
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 2))).day  # дата заезда
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(3, 9))).day  # дата выезда
        user_data['checkin'] = checkin
        user_data['checkout'] = checkout

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_report_page._open(path=admin_report_page.path)
        admin_report_page.assert_calendar()

        admin_report_page.choose_calendar_dates(
            checkin=user_data['checkin'],
            checkout=user_data['checkout'],
        )
        admin_report_page.assert_booking_window()

        admin_report_page.enter_value_into_field(field_name='firstname', value=user_data['firstname'])
        admin_report_page.enter_value_into_field(field_name='lastname', value=user_data['lastname'])
        admin_report_page.select_value_in_dropdown(field_name='room_number', value=room_info['room_number'])
        admin_report_page.select_value_in_dropdown(field_name='deposit_paid', value=choice(['true', 'false']))
        admin_report_page.click_book_btn()

        admin_main_page._open(path=admin_main_page.path)
        admin_main_page.assert_open_admin_main_page()

        admin_main_page.click_room_by_room_number(room_number=room_info['room_number'])
        admin_room_details_page.assert_open_room_details_page(room_number=room_info['room_number'])

        booking_list = admin_room_details_page.get_reservation_list()
        current_booking = choice(
            [
                x for x in booking_list if x['firstname'] == user_data['firstname'] and
                x['lastname'] == user_data['lastname']
            ]
        )

        expected_total_price = (user_data['checkout'] - user_data['checkin'] + 1) * \
            int(room_info['room_price'])
        assert expected_total_price == int(current_booking['price']), 'Неверная итоговая цена'
        assert user_data['checkin'] == int(current_booking['checkin'][-2:])
        assert user_data['checkout'] == int(current_booking['checkout'][-2:])

    @title('Отмена бронирования через админ-панель')
    @pytest.mark.no_parallel
    def test_admin_panel_booking_cancellation(
        self, add_room, admin_main_page, admin_login_page, admin_report_page, admin_room_details_page,
    ):

        # подготовка тестовых данных
        add_room(room_availability=True)
        user_data = random_user_data()
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 2))).day  # дата заезда
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(3, 9))).day  # дата выезда
        user_data['checkin'] = checkin
        user_data['checkout'] = checkout

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_report_page._open(path=admin_report_page.path)
        admin_report_page.assert_calendar()

        admin_report_page.choose_calendar_dates(
            checkin=user_data['checkin'],
            checkout=user_data['checkout'],
        )
        admin_report_page.assert_booking_window()
        admin_report_page.click_cancel_btn()

        admin_report_page.assert_calendar()

    @title('Проверка информации по бронированию в админ-панели')
    @pytest.mark.no_parallel
    @pytest.mark.xfail(reason='Неверно проставляется дата выезда')
    def test_assert_user_booking_in_admin_panel(
        self, main_page, admin_login_page, add_main_page_booking, admin_main_page, admin_room_details_page,
    ):
        # бронирование номера пользователем с главной страницы сайта
        room_info, user_booking_info = add_main_page_booking

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_main_page.click_room_by_room_number(room_number=room_info['room_number'])
        admin_room_details_page.assert_open_room_details_page(room_number=room_info['room_number'])

        booking_list = admin_room_details_page.get_reservation_list()
        current_booking = choice(
            [
                x for x in booking_list if x['firstname'] == user_booking_info['firstname'] and
                x['lastname'] == user_booking_info['lastname']
            ]
        )

        expected_total_price = (user_booking_info['checkout'] - user_booking_info['checkin'] + 1) * \
            int(room_info['room_price'])
        assert expected_total_price == int(current_booking['price']), 'Неверная итоговая цена'
        assert user_booking_info['checkin'] == int(current_booking['checkin'][-2:])
        assert user_booking_info['checkout'] == int(current_booking['checkout'][-2:])

    @title('Удаление бронирования')
    @pytest.mark.no_parallel
    def test_delete_booking(
        self, main_page, admin_login_page, add_main_page_booking, admin_main_page, admin_room_details_page,
    ):
        # бронирование номера пользователем с главной страницы сайта
        room_info, user_booking_info = add_main_page_booking

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_main_page.click_room_by_room_number(room_number=room_info['room_number'])
        admin_room_details_page.assert_open_room_details_page(room_number=room_info['room_number'])

        booking_list = admin_room_details_page.get_reservation_list()
        current_booking = choice(
            [
                x for x in booking_list if x['firstname'] == user_booking_info['firstname'] and
                x['lastname'] == user_booking_info['lastname']
            ]
        )

        admin_room_details_page.click_delete_btn_by_firstname(firstname=current_booking['firstname'])
        new_current_booking = ''
        for _ in range(5):
            new_booking_list = admin_room_details_page.get_reservation_list()
            new_current_booking = [
                x for x in new_booking_list if x['firstname'] == user_booking_info['firstname'] and
                x['lastname'] == user_booking_info['lastname']
            ]
            if len(new_current_booking) == 0:
                break
            sleep(1)
        assert len(new_current_booking) == 0, 'Бронирование не было удалено'
