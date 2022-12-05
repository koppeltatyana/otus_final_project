from allure import suite, title


@suite('[Pytest][UI]')
class TestMainPage:
    """
    Класс для ui-тестов главной страницы сайта
    """

    @title('Проверить отображение карты на главной странице сайта')
    def test_map_main_page(self, main_page):
        main_page._open()
        main_page.close_welcome_msg()
        main_page.assert_map_on_the_main_page()
