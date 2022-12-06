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

    @title('Проверка информации по бронированию в админ-панели')
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
    def test_delete_booking(
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
