from json import load
from os.path import join
from pathlib import Path
from random import choice, sample, randint
import string

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
import mimesis.exceptions
from mimesis import Person

from api import ApiBooking


def get_settings():
    ROOT_DIR = Path(__file__).parent.parent
    CONFIG_PATH = join(ROOT_DIR, 'config/config.json')
    with open(CONFIG_PATH) as data:
        config = load(data)
    return config


def asserts(response, name):
    """
    A method for verifying the validation of a test result based on a json schema

    :param response: Response from the server
    :param name: JSON schema name
    """

    def validate_json(_response, _name):
        root_dir = Path(__file__).parent.parent
        json_schema_path = join(root_dir, 'json_schema', _name + '.json')

        with open(json_schema_path) as file:
            json_file = load(file)
        try:
            validate(instance=_response, schema=json_file)
            return True
        except mimesis.exceptions.SchemaError:
            print('Схема содержит ошибку')
        except ValidationError as e:
            print('Ошибка', e)
        except Exception as e:
            print(e)
        return False

    assert validate_json(_response=response, _name=name), f'Ошибка при валидации схемы - {name}'


def get_random_booking_ids_list(count: int = 5) -> list[str]:
    """
    Получить список случайных идентификаторов бронирований.

    :param count: количество id, которое необходимо сформировать.
    :return: список идентификаторов бронирований в формате списка строк
    """
    api_booking = ApiBooking(api_base_url=get_settings()['SOURCE']['API_URL'])
    response = api_booking.get_booking_ids()[0]
    booking_id_list = [x['bookingid'] for x in response]
    return sample(booking_id_list, count)


def get_random_booking_client_data_list(count: int = 5) -> list[dict]:
    """
    Получить список случайных данных клиентов с бронированиями

    :param count: количество клиентских данных, которое необходимо сформировать.
    :return: список клиентских данных
    """
    clients_data_list = []
    api_booking = ApiBooking(api_base_url=get_settings()['SOURCE']['API_URL'])
    booking_id_list = sample([x['bookingid'] for x in api_booking.get_booking_ids()[0]], count)
    for booking_id in booking_id_list:
        clients_data_list += [
            api_booking.get_booking_info_by_id(booking_id=booking_id)[0]
        ]
    return clients_data_list


def get_random_booking_clients_name_list(count: int = 5) -> list[dict]:
    """
    Получение списка имен клиентов

    :param count: количество клиентских имен, которое необходимо сформировать.
    :return: список имен клиентов
    """
    clients_name_list = []
    clients_data_list = get_random_booking_client_data_list(count=count)
    for client in clients_data_list:
        clients_name_list += [
            {
                'firstname': client['firstname'],
                'lastname': client['lastname'],
            }
        ]
    return clients_name_list


def get_random_booking_clients_residence_date_list(count: int = 5) -> list[dict]:
    """
    Получение списка дат пребывания клиентов

    :param count: количество клиентских дат пребывания, которое необходимо сформировать.
    :return: список дат пребывания
    """
    residence_date_list = []
    clients_data_list = get_random_booking_client_data_list(count=count)
    for client in clients_data_list:
        residence_date_list += [
            {
                'checkin': client['bookingdates']['checkin'],
                'checkout': client['bookingdates']['checkout'],
            }
        ]
    return residence_date_list


def random_email(char_num: int = 5) -> str:
    return ''.join(choice(string.ascii_lowercase) for _ in range(char_num)) + choice(['gmail.com', 'mail.ru'])


def random_string(char_num: int = 5) -> str:
    return ''.join(choice(string.ascii_lowercase) for _ in range(char_num))


def random_phone() -> str:
    return ''.join(choice(string.digits) for _ in range(10))


def random_user_firstname() -> str:
    return Person().first_name()


def random_user_lastname() -> str:
    return Person().last_name()


def random_user_data() -> dict:
    """
    Сгенерировать пользовательские данные

    :return: рандомные данные пользователя в формате словаря
    """

    return {
        'firstname': random_user_firstname(),
        'lastname': random_user_lastname(),
        'email': random_email(),
        'phone': random_phone(),
    }


def random_room_data(availability: bool = True) -> dict:
    """
    Сгенерировать данные для номера

    :param availability: возможность бронирования номера
    :return: рандомные данные номера в формате словаря
    """

    room_accessibility = 'true' if availability is True else 'false'
    return {
        'room_number': str(randint(150, 500)),
        'room_type': choice(['Single', 'Twin', 'Double', 'Family', 'Suite']),
        'room_accessibility': room_accessibility,
        'room_price': str(randint(100, 1000)),
        'room_details': sample(['WiFi', 'Refreshments', 'TV', 'Safe', 'Radio', 'Views'], randint(1, 6)),
        'room_description': random_string(char_num=50),
        'room_image': choice(
            [
                'https://www.mwtestconsultancy.co.uk/img/testim/room2.jpg',
                'https://www.mwtestconsultancy.co.uk/img/testim/room2.jpg',
                'https://miro.medium.com/max/1400/1*-Vt3v_GlyEtTCiGtQpbHww.png',
            ]
        )
    }
