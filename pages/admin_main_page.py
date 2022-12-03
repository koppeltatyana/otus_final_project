from allure_commons._allure import step

from locators import AdminMainPageLocators as Locators
from pages.base_page import BasePage


class AdminMainPage(BasePage):
    """
    Класс для хранения методов главной странице админ-панели
    """

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    def get_available_room_list(self):
        """
        Получить список доступных для бронирования номеров

        :return: список номеров в формате словаря
        """
        room_list = []
        room_items = self.find_elements(Locators.ROOM_ITEM)
        for room_item in room_items:
            room_number = room_item.find_element(*Locators.ROOM_NUMBER).text
            room_type = room_item.find_element(*Locators.ROOM_TYPE).text
            room_accessibility = room_item.find_element(*Locators.ROOM_ACCESSIBLE).text
            room_price = room_item.find_element(*Locators.ROOM_PRICE).text
            room_details = room_item.find_element(*Locators.ROOM_DETAILS).text
            room_list += [
                {
                    'room_number': room_number,
                    'room_type': room_type,
                    'room_accessibility': room_accessibility,
                    'room_price': room_price,
                    'room_details': room_details,
                }
            ]
        return room_list

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить авторизацию админом')
    def assert_open_admin_main_page(self):
        """
        Проверка открытия главной страницы админ-панели
        """
        self.find_element(Locators.LOGOUT_BTN)
