from time import sleep

from allure import suite, title

from data.data import UI_ADMIN_USER
from utils.helpers import random_email, random_phone, random_string


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

    @title('Изменение контактных данных сайта')
    def test_contact_data_editing(self, admin_login_page, admin_main_page, admin_branding_page, main_page):
        contact_data = {
            'contact_name': random_string(char_num=10),
            'contact_address': random_string(char_num=50),
            'contact_phone': random_phone(),
            'contact_email': random_email(),
        }

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

        admin_branding_page.enter_value_into_field_name(field_name='contact_name', value=contact_data['contact_name'])
        admin_branding_page.enter_value_into_field_name(
            field_name='contact_address', value=contact_data['contact_address'])
        admin_branding_page.enter_value_into_field_name(field_name='contact_phone', value=contact_data['contact_phone'])
        admin_branding_page.enter_value_into_field_name(field_name='contact_email', value=contact_data['contact_email'])
        admin_branding_page.click_submit_btn()
        admin_branding_page.click_close_alert_btn()

        admin_main_page.click_front_page_btn()
        sleep(3)
        main_page.assert_open_main_page()
        main_page.assert_contact_info(
            expected_name=contact_data['contact_name'],
            expected_address=contact_data['contact_address'],
            expected_email=contact_data['contact_email'],
            expected_phone=contact_data['contact_phone'],
        )
