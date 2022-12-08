import datetime
from random import randint

from _pytest.fixtures import fixture

from api import ApiAuth, ApiBooking
from data.data import API_ADMIN_USER
from utils.helpers import get_settings, get_random_booking_ids_list, get_random_booking_clients_name_list, \
    get_random_booking_clients_residence_date_list, random_user_data


@fixture(scope='function')
def api_auth():
    return ApiAuth(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_booking():
    return ApiBooking(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function', params=get_random_booking_ids_list(count=5))
def api_booking_id(request):
    return request.param


@fixture(scope='function', params=get_random_booking_clients_name_list())
def api_booking_clients_name(request):
    return request.param


@fixture(scope='function', params=get_random_booking_clients_residence_date_list())
def api_booking_clients_residence_date(request):
    return request.param


@fixture(scope='function')
def access_token(api_auth):
    token = api_auth.admin_panel_login(
        username=API_ADMIN_USER['username'],
        password=API_ADMIN_USER['password'],
    )[0]['token']
    return token


@fixture(scope='function')
def api_create_booking(api_booking):
    checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 5))).strftime('%Y-%m-%d')
    checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(5, 30))).strftime('%Y-%m-%d')
    created_booking = api_booking.create_booking(
        firstname=random_user_data()['firstname'],
        lastname=random_user_data()['lastname'],
        total_price=randint(100, 1000),
        checkin=checkin,
        checkout=checkout,
        additional_needs='Qwe',
        deposit_paid=True,
    )[0]
    return created_booking
