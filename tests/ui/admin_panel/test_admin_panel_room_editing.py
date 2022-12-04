from random import choice
from time import sleep

from allure import suite, title

from data.data import UI_ADMIN_USER
from utils.helpers import random_room_data


@suite('[Pytest][UI]')
class TestAdminPanelAuth:
    """
    Класс для ui-тестов по добавлению, удалению и редактированию информации по номерам в админ-панели
    """

    @title('Проверка добавления номера для бронирования в админке')
    def test_admin_panel_room_adding(self, admin_login_page, admin_main_page):
        room_info = random_room_data(availability=True)

        admin_login_page._open(path=admin_login_page.path)
        admin_login_page.close_welcome_msg()
        admin_login_page.assert_open_admin_panel_login_page()  # проверить открытие страницы авторизации в админку

        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )  # авторизация в админ-панель
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        old_room_list = admin_main_page.get_available_room_list()
        admin_main_page.enter_value_into_text_field(
            field_name='room_number',
            value=room_info['room_number'],
        )  # ввод значения в текстовое поле номера комнаты
        admin_main_page.select_value_in_dropdown(field_name='room_type', value=room_info['room_type'])
        admin_main_page.select_value_in_dropdown(field_name='room_accessibility', value=room_info['room_accessibility'])
        admin_main_page.enter_value_into_text_field(
            field_name='room_price',
            value=room_info['room_price'],
        )  # ввод значения в текстовое поле стоимости номера
        for room_detail in room_info['room_details']:
            admin_main_page.click_checkbox_by_name(checkbox_name=room_detail)
        admin_main_page.click_create_btn()  # клик по кнопке "Create"

        for _ in range(5):
            actual_room_list = admin_main_page.get_available_room_list()
            if len(actual_room_list) > len(old_room_list):
                break
            sleep(1)

        assert room_info['room_number'] in [x['room_number'] for x in admin_main_page.get_available_room_list()], \
            'Номер не был добавлен'

        added_room = choice(
            [
                x for x in admin_main_page.get_available_room_list()
                if x['room_number'] == room_info['room_number']
            ]
        )  # получить информацию с ui для добавленного номера

        assert added_room['room_type'] == room_info['room_type'], \
            f'Тип номера не соответствует ожидаемому. ОР: {room_info["room_type"]}. ФР: {added_room["room_type"]}'
        assert added_room['room_accessibility'] == room_info['room_accessibility'], \
            f'Возможность бронирования номера не соответствует ожидаемому. ' \
            f'ОР: {room_info["room_accessibility"]}. ФР: {room_info["room_accessibility"]}.'
        assert added_room['room_price'] == room_info['room_price'], \
            f'Стоимость номера не соответствует ожидаемой. ' \
            f'ОР: {room_info["room_price"]}. ФР: {added_room["room_price"]}.'
        assert sorted(added_room['room_details']) == sorted(room_info['room_details']), \
            'Детали номера не соответствуют ожидаемым. ' \
            f'ОР: {sorted(room_info["room_details"])}. ФР: {sorted(added_room["room_details"])}.'

    @title('Проверка добавления номера для бронирования в админке')
    def test_admin_panel_room_deleting(self, admin_login_page, admin_main_page, add_room):
        added_room = add_room(room_availability=True)

        admin_main_page._open(path=admin_main_page.path)
        admin_login_page.admin_panel_login(
            username=UI_ADMIN_USER['username'],
            password=UI_ADMIN_USER['password'],
        )
        admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

        admin_main_page.click_delete_btn_by_room_number(room_number=added_room['room_number'])
        try:
            actual_room_list = admin_main_page.get_available_room_list()
            assert added_room['room_number'] not in [x['room_number'] for x in actual_room_list], \
                f'Комната "{added_room["room_number"]}" не была удалена.'
        except Exception:
            sleep(1)
