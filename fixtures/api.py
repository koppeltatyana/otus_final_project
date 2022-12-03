from _pytest.fixtures import fixture

from api.api_auth import ApiAuth
from data.data import ADMIN_USER
from utils.helpers import random_user_data, get_settings


@fixture(scope='function')
def api_auth():
    return ApiAuth(api_base_url=get_settings()['SOURCE']['API_URL'])


@fixture(scope='session')
def access_token(api_auth):
    token = api_auth.admin_panel_login(
        login=ADMIN_USER['username'],
        password=ADMIN_USER['password'],
    )[0]['token']
    return token


@fixture(scope='function')
def api_create_user(api_auth, api_app_key, api_app_token):
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
            signup_token=api_app_token,
        )
        return user_data
    return wrapper
