import allure

from api.base_api import BaseApi


class ApiHotels(BaseApi):
    """
    Класс для хранения апи-методов по сервису бронирования отелей
    """

    @allure.step('Поиск отелей в городе {city}')
    def search_hotels(
        self, app_key: str, city: str, checkin: str, checkout: str, nationality: str, adults_count: int,
        children_count: int, rooms: str, lang: str, currency: str, ip: str,
    ):

        response = self._post(
            url=f'api/hotel/search?appKey={app_key}',
            data={
                'city': city,
                'checkin': checkin,
                'checkout': checkout,
                'nationality': nationality,
                'adults': adults_count,
                'chlids': children_count,
                'rooms': rooms,
                'lang': lang,
                'currency': currency,
                'ip': ip,
                'browser_version': 'chrome',
                'type': 'postman',
                'os': 'windows',
            }
        )
        try:
            return response.json(), response.status_code
        except Exception:
            return '', response.status_code

