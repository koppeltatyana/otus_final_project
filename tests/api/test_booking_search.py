import pytest
from allure import suite, title

from utils.helpers import asserts


@suite('[Pytest][API]')
class TestBookingSearch:
    """
    Класс для апи-тестов по поиску бронирований
    """

    @title('Получение списка всех идентификаторов бронирований')
    def test_getting_all_booking_ids(self, api_booking):
        response, status_code = api_booking.get_booking_ids()
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_ids',
        )

    @title('Получение списка идентификаторов бронирований по имени и фамилии с данными {api_booking_clients_name}')
    def test_getting_booking_ids_by_client_name(self, api_booking, api_booking_clients_name):
        response, status_code = api_booking.get_booking_ids(
            first_name=api_booking_clients_name['firstname'],
            last_name=api_booking_clients_name['lastname'],
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_ids',
        )

    @title('Получение списка идентификаторов бронирований по дате заезда и выезда с данными '
           '{api_booking_clients_residence_date}')
    @pytest.mark.no_parallel
    def test_getting_booking_ids_by_residence_date(self, api_booking, api_booking_clients_residence_date):
        response, status_code = api_booking.get_booking_ids(
            checkin=api_booking_clients_residence_date['checkin'],
            checkout=api_booking_clients_residence_date['checkout'],
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_ids',
        )

    @title('Получение информации по бронированию по идентификатору "{api_booking_id}"')
    @pytest.mark.no_parallel
    def test_get_booking_info_by_id(self, api_booking, api_booking_id):
        response, status_code = api_booking.get_booking_info_by_id(
            booking_id=api_booking_id,
        )
        assert status_code == 200
        asserts(
            response=response,
            name='booking/get_booking_info',
        )

    @title('Получение информации по бронированию по несуществующему идентификатору "{booking_id}"')
    @pytest.mark.parametrize('booking_id', [1, 0])
    def test_get_booking_info_by_non_existent_id(self, api_booking, booking_id):
        response, status_code = api_booking.get_booking_info_by_id(
            booking_id=booking_id,
        )
        assert status_code == 404
        assert response == 'Not Found'
