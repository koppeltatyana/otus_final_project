from selenium.webdriver.common.by import By


class AdminBrandingPageLocators:
    """
    Класс для хранения методов страницы номера админ-панели
    """

    path = '/#/admin/report'

    # Заголовок страницы
    TITLE = (By.XPATH, './/h2[text()="B&B details"]')
    # Поле ввода описания
    DESC_INPUT = (By.ID, 'description')
    # Поле ввода названия сайта в блоке контактной информации
    CONTACT_NAME_INPUT = (By.ID, 'contactName')
    # Поле ввода адреса в блоке контактной информации
    CONTACT_PHONE_INPUT = (By.ID, 'contactPhone')
    # Поле ввода телефона в блоке контактной информации
    CONTACT_ADDRESS_INPUT = (By.ID, 'contactAddress')
    # Поле ввода телефона в блоке контактной информации
    CONTACT_EMAIL_INPUT = (By.ID, 'contactEmail')
    # Кнопка "Update"
    SUBMIT_BTN = (By.ID, 'updateBranding')
    # Кнопка "Close" в алерте
    CLOSE_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary" and text()="Close"]')
