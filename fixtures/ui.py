import datetime
from random import randint
from time import sleep

from _pytest.fixtures import fixture

from data.data import UI_ADMIN_USER
from pages import MainPage, AdminMainPage, AdminLoginPage, AdminReportPage, AdminRoomDetailsPage, AdminBrandingPage
from utils.helpers import random_room_data, random_user_data


@fixture(scope='function')
def admin_branding_page(browser):
    return AdminBrandingPage(browser)


@fixture(scope='function')
def admin_login_page(browser):
    return AdminLoginPage(browser)


@fixture(scope='function')
def admin_main_page(browser):
    return AdminMainPage(browser)


@fixture(scope='function')
def admin_report_page(browser):
    return AdminReportPage(browser)


@fixture(scope='function')
def admin_room_details_page(browser):
    return AdminRoomDetailsPage(browser)


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)


@fixture(scope='function')
def add_room(admin_login_page, admin_main_page):
    """ Фикстура для добавления комнаты """

    def wrapper(room_availability: bool = True):
        room_info = random_room_data(availability=room_availability)

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
        admin_main_page.click_logout_btn()
        return room_info

    return wrapper


room_for_deleting = {}


@fixture(scope='function')
def delete_room_after_test(admin_login_page, admin_main_page):
    """ Фикстура для удаления номера после теста """

    global room_for_deleting

    def wrapper(room_number: str):
        room_for_deleting['room_number'] = room_number
        return room_for_deleting

    yield wrapper

    admin_login_page._open(path=admin_login_page.path)
    admin_login_page.close_welcome_msg()

    admin_login_page.admin_panel_login(
        username=UI_ADMIN_USER['username'],
        password=UI_ADMIN_USER['password'],
    )  # авторизация в админ-панель
    admin_main_page.assert_open_admin_main_page()  # проверить открытие главной страницы админ-панели

    old_room_list = admin_main_page.get_available_room_list()

    admin_main_page.click_delete_btn_by_room_number(room_number=room_for_deleting['room_number'])
    for _ in range(5):
        actual_room_list = admin_main_page.get_available_room_list()
        if len(actual_room_list) < len(old_room_list):
            break
        sleep(1)
    admin_main_page.click_logout_btn()


@fixture(scope='function')
def add_main_page_booking(add_room, main_page):
    """ Фикстура для бронирования номера с главной страницы """

    # тестовые данные
    room_info = add_room(room_availability=True)  # создание нового номера без бронирований
    user_data = random_user_data()  # получение данных пользователя
    checkin = (datetime.datetime.today() + datetime.timedelta(days=randint(1, 2))).day  # дата заезда
    checkout = (datetime.datetime.today() + datetime.timedelta(days=randint(3, 9))).day  # дата выезда
    user_data['checkin'] = checkin
    user_data['checkout'] = checkout

    main_page._open()
    main_page.close_welcome_msg()
    main_page.assert_open_main_page()

    ui_room_list = main_page.get_main_page_room_list()  # получить список номеров с главной странице
    room_index = len(ui_room_list) - 1  # получить индекс бронируемого номера

    main_page.click_booking_btn_by_index(room_index=room_index)  # кликнуть по кнопке "Booking this room"
    main_page.assert_calendar()  # проверить появление календаря на странице для выбора дат бронирования

    main_page.choose_calendar_dates(checkin=checkin, checkout=checkout)  # выбор дат бронирования

    # заполнение персональных данных
    main_page.enter_value_into_field(field_name='firstname', value=user_data['firstname'])
    main_page.enter_value_into_field(field_name='lastname', value=user_data['lastname'])
    main_page.enter_value_into_field(field_name='email', value=user_data['email'])
    main_page.enter_value_into_field(field_name='phone', value=user_data['phone'])
    main_page.click_book_btn()  # клик по кнопке "Book"

    main_page.assert_booking_successful_modal_window()
    main_page.click_close_successful_modal_window()  # закрыть модальное окно после успешного бронирования
    return room_info, user_data
