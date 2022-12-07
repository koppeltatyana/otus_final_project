from allure import suite, title

from data.data import API_ADMIN_USER
from utils.helpers import asserts, random_string


@suite('[Pytest][API]')
class TestAuth:
    """
    Класс для апи-тестов по авторизации
    """

    @title('Авторизация пользователем в админ-панели')
    def test_admin_panel_login(self, api_auth):
        response, status_code = api_auth.admin_panel_login(
            username=API_ADMIN_USER['username'],
            password=API_ADMIN_USER['password'],
        )
        assert status_code == 200
        asserts(
            response=response,
            name='auth/valid_login',
        )

    @title('Невалидный логин')
    def test_invalid_login(self, api_auth):
        response, status_code = api_auth.admin_panel_login(
            username=random_string(),
            password=random_string(),
        )
        assert status_code == 200
        asserts(
            response=response,
            name='auth/invalid_login',
        )

    @title('Проверка работоспособности сайта')
    def test_site_health(self, api_auth):
        response, status_code = api_auth.check_health()
        assert status_code == 201, f'Статус код запроса не соответствует ожидаемому. ОР: 201. ФР: {status_code}'
        assert response == 'Created', f'Тело ответа не соответствует ожидаемому. ОР: "Created". ФР: "{response}"'
