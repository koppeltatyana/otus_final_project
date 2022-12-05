from allure_commons._allure import step

from pages.base_page import BasePage
from locators import MainPageLocators as Locators


class MainPage(BasePage):
    """
    Класс для хранения методов главной страницы
    """

    # -------------------------------------------------- Действия ---------------------------------------------------- #
    def get_main_page_room_list(self):
        """
        Получить список номеров с главной страницы

        :return: список номеров и их описаний
        """
        room_list = []
        room_items = self.find_elements(Locators.ROOM_ITEM)
        for item in room_items:
            room_list += [
                {
                    'room_type': item.find_element(*Locators.ROOM_TYPE).text,
                    'room_description': item.find_element(*Locators.ROOM_DESCRIPTION).text,
                    'room_details': [x.text for x in item.find_elements(*Locators.ROOM_DETAILS)]
                }
            ]
        return room_list

    # -------------------------------------------------- Проверки ---------------------------------------------------- #
    @step('Проверить отображение карты на главной странице сайта')
    def assert_map_on_the_main_page(self):
        """ Проверка отображения карты на главной странице сайта """
        assert self.is_element_present(Locators.MAP), 'На главной странице сайта нет карты'
