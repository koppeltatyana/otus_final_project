import allure

from api.base_api import BaseApi


class ApiMainInfo(BaseApi):
    """
    Класс для хранения апи-методов по получению основной информации
    """

    @allure.step('Получить главную информацию сайта')
    def get_main_info(self, app_key: str):
        """
        Получить главную информацию сайта

        :param app_key: ключ приложения (поставляется с демо)
        :return: ответ в формате словаря
        """
        response = self._get(
            url=f'api/main/app?appKey={app_key}&lang=en&currency=usd'
        )
        return response.json(), response.status_code
