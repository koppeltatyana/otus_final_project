import allure

from api.base_api import BaseApi


class ApiAuth(BaseApi):
    """
    Класс для хранения апи-методов по авторизации, регистрации и смене пароля
    """

    @allure.step('Авторизация на сайте с логином {email} и паролем {password}')
    def login(self, email: str, password: str, app_key: str) -> (dict, int):
        """
        Авторизоваться на сайте

        :param app_key: ключ приложения (поставляется с демо)
        :param email: электронная почта пользователя
        :param password: пароль пользователя
        :return: кортеж из двух элементов: ответ в формате словаря и статус код ответа
        """
        data = {
            'email': email,
            'password': password
        }
        response = self._post(
            url=f'api/login/check?appKey={app_key}',
            data=data,
        )
        return response.json(), response.status_code

    @allure.step('Регистрация на сайте с переданными данными пользователя')
    def signup(
        self, first_name: str, last_name: str, email: str, password: str, phone: str, status: str, user_type: str,
        signup_token: str, app_key: str,
    ) -> (dict, int):
        """
        Получить главную информацию сайта

        :param app_key: ключ приложения (поставляется с демо)
        :param first_name: имя пользователя
        :param last_name: фамилия пользователя
        :param email: электронная почта пользователя
        :param password: пароль пользователя
        :param phone: телефон пользователя
        :param status: статус активности пользователя (yes, no)
        :param user_type: тип пользователя
        :param signup_token: регистрационный токен
        :return: кортеж из двух элементов: ответ в формате словаря и статус код ответа
        """
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'phone': phone,
            'status': status,
            'type': user_type,
            'signup_token': signup_token,
        }
        response = self._post(
            url=f'api/login/signup?appKey={app_key}',
            data=data,
        )
        return response.json(), response.status_code

    @allure.step('Сбросить пароль пользователя с логином {email}')
    def reset_password(self, app_key: str, email: str) -> (dict,  int):
        """
        Сброс пароля пользователя

        :param app_key: ключ приложения (поставляется с демо)
        :param email: электронная почта пользователя
        :return: кортеж из двух элементов: ответ в формате словаря и статус код ответа
        """

        response = self._post(
            url=f'api/login/reset_password?appKey={app_key}',
            data={
                'email': email,
            },
        )
        return response.json(), response.status_code
