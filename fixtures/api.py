from _pytest.fixtures import fixture

from api import ApiAuth, ApiBooking
from data.data import API_ADMIN_USER
from utils.helpers import get_settings, get_random_booking_ids_list, get_random_booking_clients_name_list, \
    get_random_booking_clients_residence_date_list


@fixture(scope='function')
def api_auth():
    return ApiAuth(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_booking():
    return ApiBooking(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function', params=get_random_booking_ids_list())
def api_booking_id(request):
    return request.param


@fixture(scope='function', params=get_random_booking_clients_name_list())
def api_booking_clients_name(request):
    return request.param


@fixture(scope='function', params=get_random_booking_clients_residence_date_list())
def api_booking_clients_residence_date(request):
    return request.param


@fixture(scope='session')
def access_token(api_auth):
    token = api_auth.admin_panel_login(
        login=API_ADMIN_USER['username'],
        password=API_ADMIN_USER['password'],
    )[0]['token']
    return token
