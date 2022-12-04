import datetime
from random import randint, choice

import pytest
from allure import suite, title

from utils.helpers import asserts, random_user_data


@suite('[Pytest][API]')
class TestBooking:
    """
    Класс для апи-тестов по бронированию
    """

    @title('Создание бронирования')
    @pytest.mark.parametrize('additional_needs', [None, 'Breakfast', ['Breakfast', 'Morning Alarm']])
    @pytest.mark.parametrize('deposit_paid', [True, False])
    def test_create_booking(self, api_booking, additional_needs, deposit_paid):
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 5))).strftime('%Y-%m-%d')
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(5, 30))).strftime('%Y-%m-%d')
        response, status_code = api_booking.create_booking(
            firstname=random_user_data()['firstname'],
            lastname=random_user_data()['lastname'],
            total_price=randint(100, 1000),
            checkin=checkin,
            checkout=checkout,
            additional_needs=additional_needs,
            deposit_paid=deposit_paid,
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/create_booking',
        )

    @title('Редактирование бронирования с id "{api_one_booking_id}"')
    @pytest.mark.parametrize('additional_needs', [None, 'Breakfast', ['Breakfast', 'Morning Alarm']])
    @pytest.mark.parametrize('deposit_paid', [True, False])
    def test_full_booking_editing(self, api_booking, access_token, additional_needs, deposit_paid, api_one_booking_id):
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 5))).strftime('%Y-%m-%d')
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(5, 30))).strftime('%Y-%m-%d')
        response, status_code = api_booking.edit_booking(
            access_token=access_token,
            booking_id=api_one_booking_id,
            firstname=random_user_data()['firstname'],
            lastname=random_user_data()['lastname'],
            total_price=randint(100, 1000),
            checkin=checkin,
            checkout=checkout,
            additional_needs=additional_needs,
            deposit_paid=deposit_paid,
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_info',
        )

    @title('Частичное редактирование бронирования с id "{api_booking_id}"')
    def test_partial_booking_editing(self, api_booking, access_token, api_booking_id):
        checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 5))).strftime('%Y-%m-%d')
        checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(5, 30))).strftime('%Y-%m-%d')
        response, status_code = api_booking.edit_booking(
            access_token=access_token,
            booking_id=api_booking_id,
            firstname=choice([None, random_user_data()['firstname']]),
            lastname=choice([None, random_user_data()['lastname']]),
            total_price=choice([None, randint(100, 1000)]),
            checkin=choice([None, checkin]),
            checkout=choice([None, checkout]),
            additional_needs=choice([None, 'Breakfast', ['Breakfast', 'Morning Alarm']]),
            deposit_paid=choice([None, True, False]),
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_info',
        )
