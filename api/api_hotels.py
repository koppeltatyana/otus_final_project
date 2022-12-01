import allure

from api.base_api import BaseApi


class ApiHotels(BaseApi):
    """
    Класс для хранения апи-методов по сервису бронирования отелей
    """

    @allure.step('Поиск отелей в городе {city}')
    def search_hotels(
        self, app_key: str, city: str, checkin: str, checkout: str, ip: str, nationality: str = 'US',
        adults_count: int = 2, children_count: int = 0, rooms: int = 1, lang: str = 'en', currency: str = 'USD',
    ) -> (dict, int):
        """
        Поиск отелей в городе

        :param app_key: ключ приложения (поставляется с демо)
        :param city: город, в котором требуется искать
        :param checkin: дата заезда
        :param checkout: дата выезда
        :param ip: ip-адрес пользователя, который производит поиск
        :param nationality: национальность гостей
        :param adults_count: количество взрослых гостей
        :param children_count: количество гостей-спиногрызов
        :param rooms: количество номеров
        :param lang: язык
        :param currency: валюта
        :return: кортеж из двух элементов: ответ в формате словаря и статус код ответа
        """

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

    @allure.step('Бронирование отеля')
    def hotel_booking(
        self, app_api_key: str, api_app_token: str, hotel_id: str, total_price: str, checkin: str, checkout: str,
        first_name: str, last_name: str, email: str, address: str, phone: str, user_id: str,  hotel_name: str,
        nights_count: str, loaction: str, hotel_img: str, stars_count: str, hotel_phone: str = '',
        hotel_email: str = '', hotel_website: str = '', adults_count: str = '2', children_count: str = '0',
    ):
        response = self._post(
            url=f'api/hotel/book?appKey={app_api_key}',
            data={
                'hotel_id': hotel_id,
                'total_price': total_price,
                'checkin': checkin,
                'checkout': checkout,
                'adults': adults_count,
                'childs': children_count,
                'deposit': '50',
                'tax': '45',
                'tax_type': 'fixed',
                'firstname': first_name,
                'lastname': last_name,
                'email': email,
                'address': address,
                'phone': phone,
                'user_id': user_id,
                'supplier': '1',
                'curr_code': 'USD',
                'deposit_type': 'percentage',
                'hotel_name': hotel_name,
                'nights': nights_count,
                'loaction': loaction,
                'hotel_img': hotel_img,
                'rooms': '1',
                'stars': stars_count,
                'hotel_phone': hotel_phone,
                'hotel_email': hotel_email,
                'hotel_website': hotel_website,
                'guest': first_name,
                'booking_from': 'postman',
                'supplier_name': 'manual',
                'token': api_app_token,
            }
        )
        return response.json(), response.status_code
