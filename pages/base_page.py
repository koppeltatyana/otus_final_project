import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url

    @allure.step('Открыть страницу {path}')
    def _open(self, path=''):
        try:
            self.driver.get(self.base_url + path)
        except Exception:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Не удалось открыть страницу {self.base_url + path}'

    @allure.step('Найти элемент с локатором {locator}')
    def find_element(self, locator, timeout=10):
        """
        Метод, возвращающий элемент по локатору locator.

        :param locator: локатор элемента
        :param timeout: время ожидания элемента (default=5)
        :return: найденный по локатору веб-элемент
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                method=EC.presence_of_element_located(locator),
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Элемент с локатором {locator} не был найден.'

    @allure.step('Найти список элементов с локатором {locator}')
    def find_elements(self, locator, timeout=10):
        """
        Метод, возвращающий список элементов по локатору locator.

        :param locator: локатор элементов
        :param timeout: время ожидания элементов (default=5)
        :return: список найденных по локатору веб-элементов
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                method=EC.presence_of_all_elements_located(locator),
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Элементы с локатором {locator} не были найдены.'

    @allure.step('Найти элемент с локатором {child_locator} внутри элемента с локатором {parent_locator}')
    def find_element_in_element(self, parent_element, child_locator: tuple):
        """
        Метод, возвращающий элемент по локатору child_locator в родительском элементе, найденному по локатору
        parent_locator

        :param parent_element: элемент-родитель
        :param child_locator: локатор элемента-потомка
        :return: элемент-потомок, найденный внутри элемента-родителя
        """
        try:
            return parent_element.find_element(*child_locator)
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Не удалось найти элемент с локатором {child_locator} внутри элемента {parent_element}'

    @allure.step('Проверить, что элемент с локатором {locator} видим на странице')
    def is_element_visible(self, locator, timeout=5):
        """
        Метод, возвращающий видимый элемент по локатору locator.

        :param locator: локатор элемента
        :param timeout: время ожидания элементов (default=5)
        :return: видимый веб-элемент
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                method=EC.visibility_of_element_located(locator),
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Элемент с локатором {locator} не виден на странице.'

    @allure.step('Проверить, что элемент с локатором {locator} кликабелен')
    def is_element_clickable(self, locator, timeout=5):
        """
        Метод, проверяющий, что элемент с локатором locator кликабельный.

        :param locator: локатор элемента
        :param timeout: время ожидания элементов (default=5)
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                method=EC.element_to_be_clickable(locator),
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Элемент с локатором {locator} не найден на странице.'

    @allure.step('Заполнить поле с локатором {locator} значением {value}')
    def fill_edit_field(self, locator, value):
        """
        Метод, заполняющий поле, найденное по локатору locator значением value

        :param locator: локатор элемента
        :param value: вводимое значение
        """
        try:
            _input = self.find_element(locator)
            _input.click()
            _input.clear()
            _input.send_keys(value)
        except Exception as ex:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Во время ввода значения {value} в поле с локатором {locator} возникла ошибка: {ex}'

    @allure.step('Кликнуть по значению {value} в выпадающем списке, найденном по локатору {locator}')
    def click_select_by_text(self, locator, value):
        """
        Метод, который находит выпадающий список по локатору locator и кликает по значению value

        :param locator: локатор элемента
        :param value: значение, которое требуется поставить в выпадающем списке
        """
        try:
            select = Select(self.find_element(locator))
            select.select_by_visible_text(value)
        except Exception as ex:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f'Во время клика по значению {value} в выпадающем списке с локатором {locator} ' \
                          f'возникла ошибка: {ex}'
