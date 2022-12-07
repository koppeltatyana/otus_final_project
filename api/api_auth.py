from json import dumps

from allure_commons._allure import step

from api.base_api import BaseApi


class ApiAuth(BaseApi):
    """
    Класс для хранения апи-методов по авторизации
    """

    @step('Проверить работоспособность сайта')
    def check_health(self) -> (str, int):
        """
        Проверка работоспособности сайта
        :return: результат выполнения запроса в формате кортежа
        """
        response = self._get(
            url='ping',
        )
        return response.text, response.status_code

    @step('Авторизоваться в админ панели с логином {username} и паролем {password}')
    def admin_panel_login(self, username: str, password: str) -> (dict, int):
        """
        Авторизация в админ панели

        :param username: логин пользователя
        :param password: пароль пользователя
        :return: результат выполнения запроса в формате кортежа (ответ в формате словаря, статус код)
        """

        response = self._post(
            url=f'auth',
            data=dumps(
                {
                    'username': username,
                    'password': password,
                },
            ),
            headers={
                'Content-Type': 'application/json',
            }
        )
        return response.json(), response.status_code
