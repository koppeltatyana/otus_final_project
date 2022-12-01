import datetime
from random import choice

import pytest
from allure import suite, title

from data.data import CURRENCIES
from utils.helpers import asserts, random_ip


@suite('[Pytest][API]')
class TestHotelsSearch:
    """
    Класс для апи-тестов по авторизации, регистрации и сбросу пароля
    """

    @title('Поиск отеля')
    @pytest.mark.parametrize('city', ['dubai'])
    def test_hotels_search(self, api_app_key, api_hotels, city):
        checkin = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        checkout = (datetime.datetime.today() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")

        response, status_code = api_hotels.search_hotels(
            app_key=api_app_key,
            city=city,
            checkin=checkin,
            checkout=checkout,
            nationality='US',
            adults_count=1,
            children_count=0,
            rooms=1,
            lang='en',
            currency=choice(CURRENCIES),
            ip=random_ip(),
        )
        assert status_code == 200
        asserts(
            response=response,
            name='hotels/search'
        )
