import datetime
from random import randint, choice
from time import sleep

import pytest
from allure import suite, title

from data.data import UI_ADMIN_USER
from utils.helpers import random_user_data, random_string


@suite('[Pytest][UI]')
class TestAdminPanelContactInfo:
    """
    Класс для ui-тестов редактирования контактной информации сайта
    """

    @title('Изменение описания сайта')
    def test_site_description_editing(self, admin_login_page, admin_main_page, admin_branding_page, main_page):
        random_desc = random_string(char_num=100)

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_main_page.click_branding_btn()
        admin_branding_page.assert_open_branding_page()

        admin_branding_page.enter_value_into_field_name(field_name='description', value=random_desc)
        admin_branding_page.click_submit_btn()
        admin_branding_page.click_close_alert_btn()

        admin_main_page.click_front_page_btn()
        sleep(3)
        main_page.assert_open_main_page()
        main_page.assert_site_description(expected_desc=random_desc)
