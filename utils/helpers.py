from json import load
from os.path import join
from pathlib import Path
from random import choice
import string

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
import mimesis.exceptions
from mimesis import Person


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


def random_email(char_num: int = 5) -> str:
    return ''.join(choice(string.ascii_lowercase) for _ in range(char_num)) + choice(['gmail.com', 'mail.ru'])


def random_phone() -> str:
    return ''.join(choice(string.digits) for _ in range(10))


def random_password(char_num: int = 5) -> str:
    return ''.join(choice(string.ascii_letters) + choice(string.digits) for _ in range(char_num))


def random_user_first_name() -> str:
    return Person().first_name()


def random_user_last_name() -> str:
    return Person().last_name()


def random_user_data(user_type: str = 'customer') -> dict:
    """
    Сгенерировать пользовательские данные

    :param user_type: тип пользователя ('customer', 'guest', 'supplier' или 'agent')
    :return: рандомные данные пользователя в формате словаря
    """

    return {
        'first_name': random_user_first_name(),
        'last_name': random_user_last_name(),
        'password': random_password(),
        'email': random_email(),
        'phone': random_phone(),
        'status': 'yes',
        'user_type': user_type,
    }
