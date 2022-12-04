from allure_commons._allure import step

from api.base_api import BaseApi


class ApiBooking(BaseApi):
    """
    Класс для хранения апи-методов по бронированию
    """

    @step('Получить список идентификаторов бронирований')
    def get_booking_ids(
            self, first_name: str = None, last_name: str = None, checkin: str = None, checkout: str = None,
    ) -> (dict, int):
        """
        Получение списка идентификаторов бронирований

        :param first_name: имя клиента (необязательное)
        :param last_name: фамилия клиента (необязательное)
        :param checkin: дата заезда (необязательное)
        :param checkout: дата выезда (необязательное)
        :return: результат выполнения запроса в формате кортежа
        """

        if first_name is not None and last_name is not None:
            url = f'booking?firstname={first_name}&lastname={last_name}'
        elif checkin is not None and checkout is not None:
            url = f'booking?checkin={checkin}&checkout={checkout}'
        else:
            url = 'booking'
        response = self._get(
            url=url,
        )
        try:
            return response.json(), response.status_code
        except Exception:
            return response.text, response.status_code

    @step('Получить информацию по бронированию по его идентификатору')
    def get_booking_info_by_id(self, booking_id: str) -> (dict, int):
        """
        Получение информации по бронированию

        :param booking_id: идентификатор бронирования
        :return: результат выполнения запроса в формате кортежа
        """
        response = self._get(
            url=f'booking/{booking_id}'
        )
        try:
            return response.json(), response.status_code
        except Exception:
            return response.text, response.status_code
