from _pytest.fixtures import fixture

from api import ApiAuth, ApiFlights, ApiHotels, ApiTours, ApiTransfers
from utils.helpers import get_settings, random_user_data


@fixture(scope='session')
def api_app_key():
    return get_settings()['API_APP_KEY']


@fixture(scope='session')
def api_signup_key():
    return get_settings()['API_SIGNUP_KEY']


@fixture(scope='function')
def api_auth():
    return ApiAuth(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_flights():
    return ApiFlights(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_hotels():
    return ApiHotels(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_tours():
    return ApiTours(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_transfers():
    return ApiTransfers(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='function')
def api_create_user(api_auth, api_app_key, api_signup_key):
    """
    Фикстура для регистрации нового пользователя
    """
    user_data = random_user_data()

    def wrapper(user_type: str = 'customer') -> dict:
        """
        Метод-обертка для регистрации нового пользователя с переданным типом пользователя

        :param user_type: тип пользователя ('customer', 'guest', 'supplier' или 'agent')
        :return: данные зарегистрированного пользователя
        """
        if user_type not in ['customer', 'guest', 'supplier', 'agent']:
            raise AssertionError('Неверно передан тип пользователя для регистрации. Допустимые типы пользователя: '
                                 '"customer", "guest", "supplier" или "agent"')
        api_auth.signup(
            app_key=api_app_key,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password'],
            email=user_data['email'],
            phone=user_data['phone'],
            status=user_data['status'],
            user_type=user_type,
            signup_token=api_signup_key,
        )
        return user_data
    return wrapper
