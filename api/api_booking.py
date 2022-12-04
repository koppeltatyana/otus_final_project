from json import dumps

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
    def get_booking_info_by_id(self, booking_id: str or int) -> (dict, int):
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

    @step('Создать бронирование')
    def create_booking(
        self, firstname: str, lastname: str, total_price: int, checkin: str, checkout: str,
        additional_needs: str or list[str] = None, deposit_paid: bool = False,
    ) -> (dict, int):
        """
        Создание бронирования

        :param firstname: имя гостя
        :param lastname: фамилия гостя
        :param total_price: конечная стоимость бронирования
        :param checkin: дата заезда (формат даты: YYYY-MM-DD)
        :param checkout: дата выезда (формат даты: YYYY-MM-DD)
        :param additional_needs: дополнительные услуги
        :param deposit_paid: оплачен ли депозит
        :return: результат выполнения запроса в формате кортежа
        """

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': total_price,
            'depositpaid': deposit_paid,
            'bookingdates': {
                'checkin': checkin,
                'checkout': checkout,
            },
            'additionalneeds': additional_needs,
        }
        response = self._post(
            url=f'booking',
            data=dumps(data),
            headers={
                'Content-Type': 'application/json',
            },
        )
        return response.json(), response.status_code

    @step('Редактировать бронирование')
    def edit_booking(
        self, access_token: str, booking_id: int, firstname: str = None, lastname: str = None, total_price: int = None,
        checkin: str = None, checkout: str = None, additional_needs: str or list = None, deposit_paid: bool = False,
    ) -> (dict, int):
        """
        Редактирование бронирования

        :param access_token: токен авторизованного админа
        :param booking_id: идентификатор бронирования
        :param firstname: имя гостя (необязательное)
        :param lastname: фамилия гостя (необязательное)
        :param total_price: конечная стоимость бронирования (необязательное)
        :param checkin: дата заезда (формат даты: YYYY-MM-DD) (необязательное)
        :param checkout: дата выезда (формат даты: YYYY-MM-DD) (необязательное)
        :param additional_needs: дополнительные услуги (необязательное)
        :param deposit_paid: оплачен ли депозит (необязательное)
        :return: результат выполнения запроса в формате кортежа (необязательное)
        """
        booking_info = self.get_booking_info_by_id(booking_id=booking_id)[0]
        if firstname is None:
            firstname = booking_info['firstname']
        if lastname is None:
            lastname = booking_info['lastname']
        if total_price is None:
            total_price = booking_info['totalprice']
        if deposit_paid is None:
            deposit_paid = booking_info['depositpaid']
        if checkin is None:
            checkin = booking_info['bookingdates']['checkin']
        if checkout is None:
            checkout = booking_info['bookingdates']['checkout']
        if additional_needs is None:
            additional_needs = booking_info['additionalneeds']

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': total_price,
            'depositpaid': deposit_paid,
            'bookingdates': {
                'checkin': checkin,
                'checkout': checkout,
            },
            'additionalneeds': additional_needs,
        }
        response = self._patch(
            url=f'booking/{booking_id}',
            data=dumps(data),
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Cookie': f'token={access_token}',
            }
        )
        return response.json(), response.status_code

    @step('Удалить бронирование')
    def delete_booking(self, access_token: str, booking_id: int) -> (str, int):
        """
        Удаление бронирования

        :param access_token: токен авторизованного админа
        :param booking_id: идентификатор бронирования
        :return: результат выполнения запроса в формате кортежа (необязательное)
        """

        response = self._delete(
            url=f'booking/{booking_id}',
            headers={
                'Content-Type': 'application/json',
                'Cookie': f'token={access_token}',
            }
        )
        return response.text, response.status_code
