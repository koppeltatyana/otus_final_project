import datetime
from random import choice

import pytest
from allure import suite, title

from data.data import CURRENCIES
from utils.helpers import asserts, random_ip, random_user_data


@suite('[Pytest][API]')
class TestHotelsBooking:
    """
    Класс для апи-тестов по авторизации, регистрации и сбросу пароля
    """

    @title('Бронирование отеля')
    @pytest.mark.parametrize('city', ['dubai'])
    def test_hotel_booking(self, api_app_key, api_app_token, api_hotels, api_auth, api_create_user, city):

        checkin = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        checkout = (datetime.datetime.today() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")

        user = api_create_user(user_type='customer')  # регистрация нового пользователя
        user_id = api_auth.login(
            app_key=api_app_key,
            email=user['email'],
            password=user['password'],
        )[0]['userInfo']['id']  # получить id пользователя

        hotel_info = choice(
            api_hotels.search_hotels(
                app_key=api_app_key,
                city=city,
                checkin=checkin,
                checkout=checkout,
                nationality='US',
                adults_count=2,
                children_count=0,
                rooms=1,
                lang='en',
                currency=choice(CURRENCIES),
                ip=random_ip(),
            )[0]
        )  # получить информацию о рандомном отеле в городе

        response, status_code = api_hotels.hotel_booking(
            app_api_key=api_app_key, api_app_token=api_app_token,
            hotel_id=hotel_info['hotel_id'],
            total_price=hotel_info['price'],
            checkin=checkin,
            checkout=checkout,
            first_name=user['first_name'],
            last_name=user['last_name'],
            email=user['email'], address='Qweqwe', phone=user['phone'], user_id=user_id,
            hotel_name=hotel_info['name'], loaction=hotel_info['location'], hotel_img=hotel_info['img'],
            nights_count='6', stars_count=hotel_info['stars'], adults_count='2', children_count='0',
        )
        assert status_code == 200
        asserts(
            response=response,
            name='hotels/booking',
        )
