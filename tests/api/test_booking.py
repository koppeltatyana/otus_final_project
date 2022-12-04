import pytest
from allure import suite, title

from utils.helpers import asserts


@suite('[Pytest][API]')
class TestBooking:
    """
    Класс для апи-тестов по бронированию
    """
