import allure

from api.base_api import BaseApi


class ApiFlights(BaseApi):
    """
    Класс для хранения апи-методов по сервису бронирования полетов
    """

    @allure.step('Поиск рейсов из {origin} в {destination}')
    def search_flights(self, app_key: str, origin: str, destination: str, flight_type: str, departure_date: str,
                       adults_count: int, children_count: int, infants_count: int, class_type: str, currency: str,
                       ip: str, return_date=None):

        response = self._post(
            url=f'api/flight/search?appKey={app_key}',
            data={
                'origin': origin,
                'destination': destination,
                'type': flight_type,
                'departure_date': departure_date,
                'return_date': return_date,
                'adults': adults_count,
                'childrens': children_count,
                'infants': infants_count,
                'class_type': class_type,
                'currency': currency,
                'ip': ip,
                'browser_version': 'chrome',
                'request_type': 'postman',
                'os': 'windows'
            }
        )
        try:
            return response.json(), response.status_code
        except Exception:
            return '', response.status_code
