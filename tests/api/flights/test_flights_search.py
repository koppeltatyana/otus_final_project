import datetime
from random import choice

import pytest
from allure import suite, title

from data.data import CURRENCIES, FLIGHTS_TICKET_TYPE
from utils.helpers import asserts, random_ip


@suite('[Pytest][API]')
class TestFlightsSearch:
    """
    Класс для апи-тестов по авторизации, регистрации и сбросу пароля
    """

    @title('Поиск рейса в одну сторону с непустым результатом поиска')
    @pytest.mark.parametrize('origin, destination', [('JKT', 'DPS'), ('CAI', 'ANK'), ('KUL', 'SIN')])
    def test_oneway_flights_search_with_non_empty_result(self, api_app_key, api_flights, origin, destination):
        departure_date = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d")

        response, status_code = api_flights.search_flights(
            app_key=api_app_key,
            origin=origin,
            destination=destination,
            flight_type='oneway',
            departure_date=departure_date,
            adults_count=1,
            children_count=0,
            infants_count=0,
            class_type=choice(FLIGHTS_TICKET_TYPE),
            currency=choice(CURRENCIES),
            ip=random_ip(),
        )
        assert status_code == 200
        asserts(
            response=response,
            name='flights/search'
        )

    @title('Поиск рейса в одну сторону с пустым результатом поиска')
    @pytest.mark.parametrize('origin, destination', [('DXB', 'RML')])
    def test_oneway_flights_search_with_empty_result(self, api_app_key, api_flights, origin, destination):
        departure_date = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')

        response, status_code = api_flights.search_flights(
            app_key=api_app_key,
            origin=origin,
            destination=destination,
            flight_type='oneway',
            departure_date=departure_date,
            adults_count=1,
            children_count=0,
            infants_count=0,
            class_type=choice(FLIGHTS_TICKET_TYPE),
            currency=choice(CURRENCIES),
            ip=random_ip(),
        )
        assert status_code == 200
        assert response == '', 'Результат поиска не пуст'

    @title('Поиск рейса в обе стороны с непустым результатом поиска')
    @pytest.mark.parametrize('origin, destination', [('CGK', 'DPS')])
    def test_return_flights_search_with_non_empty_result(self, api_app_key, api_flights, origin, destination):
        departure_date = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        return_date = ((datetime.datetime.today() + datetime.timedelta(days=6)).strftime("%Y-%m-%d"))

        response, status_code = api_flights.search_flights(
            app_key=api_app_key,
            origin=origin,
            destination=destination,
            flight_type='oneway',
            departure_date=departure_date,
            return_date=return_date,
            adults_count=1,
            children_count=0,
            infants_count=0,
            class_type=choice(FLIGHTS_TICKET_TYPE),
            currency=choice(CURRENCIES),
            ip=random_ip(),
        )
        assert status_code == 200
        asserts(
            response=response,
            name='flights/search'
        )
