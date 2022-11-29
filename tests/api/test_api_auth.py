import pytest
from allure import suite, title

from data.users import ADMIN_USER, AGENT_USER, CUSTOMER_USER, SUPPLIER_USER
from utils.helpers import asserts, random_email, random_password, random_user_first_name, random_user_last_name, \
    random_user_data


@suite('[Pytest][API]')
class TestApiAuthorization:
    """
    Класс для апи-тестов по авторизации, регистрации и сбросу пароля
    """

    @title('Авторизация пользователем с разными ролями')
    @pytest.mark.parametrize(
        'email, password',
        [
            (CUSTOMER_USER['email'], CUSTOMER_USER['password']),
            (ADMIN_USER['email'], ADMIN_USER['password']),
            (AGENT_USER['email'], AGENT_USER['password']),
            (SUPPLIER_USER['email'], SUPPLIER_USER['password'])
        ]
    )
    def test_user_login(self, api_app_key, api_auth, email, password):
        response, status_code = api_auth.login(
            app_key=api_app_key,
            email=email,
            password=password
        )
        assert status_code == 200
        asserts(
            response=response,
            name='valid_login'
        )

    @title('Невалидный логин')
    def test_invalid_login(self, api_app_key, api_auth):
        response, status_code = api_auth.login(
            app_key=api_app_key,
            email=random_email(),
            password=random_password()
        )
        assert status_code == 200
        asserts(
            response=response,
            name='invalid_login'
        )

    @title('Регистрация пользователя')
    @pytest.mark.parametrize('user_type', ['customer', 'guest', 'supplier', 'agent'])
    def test_signup(self, api_app_key, api_signup_key, api_auth, user_type):
        user_data = random_user_data(user_type=user_type)

        response, status_code = api_auth.signup(
            app_key=api_app_key,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password'],
            email=user_data['email'],
            phone=user_data['phone'],
            status=user_data['status'],
            user_type=user_data['user_type'],
            signup_token=api_signup_key,
        )
        assert status_code == 200
        asserts(
            response=response,
            name='signup'
        )

    @title('Сброс пароля пользователя')
    def test_password_reset(self, api_app_key, api_signup_key, api_auth, api_create_user):
        user = api_create_user(user_type='customer')

        response, status_code = api_auth.reset_password(
            app_key=api_app_key,
            email=user['email']
        )
        assert status_code == 200
        asserts(
            response=response,
            name='password_reset'
        )
