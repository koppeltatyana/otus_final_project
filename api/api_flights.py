import allure

from api.base_api import BaseApi


class ApiFlights(BaseApi):
    """
    Класс для хранения апи-методов по сервису бронирования полетов
    """

    @allure.step('Поиск рейсов из {origin} в {destination}')
    def search_flights(
        self, app_key: str, origin: str, destination: str, flight_type: str, departure_date: str, currency: str,
        ip: str, adults_count: int = 1, children_count: int = 0, infants_count: int = 0, class_type: str = 'economy',
        return_date=None,
    ):
        """
        Поиск рейсов на самолет

        :param app_key: ключ приложения (поставляется с демо)
        :param origin: пункт отправления
        :param destination: пункт назначения
        :param flight_type: тип полета (в одну сторону или в обе - oneway и return соответственно)
        :param departure_date: дата вылета
        :param currency: валюта
        :param ip: ip-адрес пользователя, который производит поиск
        :param adults_count: количество взрослых пассажиров
        :param children_count: количество детенышей
        :param infants_count: количество детенышей определенного возраста
        :param class_type: класс полета (economy, economy_premium, business или first)
        :param return_date: дата обратного самолета (может быть None, когда flight_type = oneway)
        :return: кортеж из двух элементов: ответ в формате словаря и статус код ответа
        """
        if flight_type != 'oneway' and return_date is None:
            raise AssertionError(
                'Чтобы найти билеты на самолет туда и обратно требуется ввести и дату вылета, и дату возвращения',
            )

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
