import datetime
from random import randint

import pytest
from allure import suite, title

from utils.helpers import asserts, random_user_data


@suite('[Pytest][API]')
class TestBooking:
    """
    Класс для апи-тестов по бронированию
    """

    @title('Создание бронирования без дополнительных нужд')
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
