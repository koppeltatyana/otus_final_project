from allure import suite, title

from utils.helpers import asserts


@suite('[Pytest][API]')
class TestApiInfo:
    """
    Класс для апи-тестов по получению информации сайта
    """

    @title('Получение главной информации сайта')
    def test_site_main_info(self, api_app_key, api_main_info):
        response, status_code = api_main_info.get_main_info(app_key=api_app_key)
        assert status_code == 200
        asserts(
            response=response,
            name='site_main_info'
        )
