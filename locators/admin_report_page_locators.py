from selenium.webdriver.common.by import By


class AdminReportPageLocators:
    """
    Класс для хранения локаторов страницы "Report" админ-панели
    """

    # Элемент календаря
    CALENDAR_ITEM = (By.XPATH, './/div[@class="rbc-month-view"]')
    # Кнопка с числом на календаре
    CALENDAR_DAY_BTN = (By.XPATH, './/button[text()="{0}"]')
    # Окно бронирования
    BOOKING_WINDOW_ITEM = (
        By.XPATH, './/div[@class="ReactModal__Content ReactModal__Content--after-open confirmation-modal"]')
    # Поле ввода имени при бронировании
    BOOKING_FIRSTNAME_INPUT = (By.NAME, 'firstname')
    # Поле ввода фамилии при бронировании
    BOOKING_LASTNAME_INPUT = (By.NAME, 'lastname')
    # Выпадающий список с выбором номера комнаты
    BOOKING_ROOM_NUMBER_SELECT = (By.ID, 'roomid')
    # Выпадающий список с выбором оплаты
    BOOKING_ROOM_PAID_SELECT = (By.ID, 'depositpaid')
    # Кнопка "Book"
    BOOK_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary float-right book-room"]')
    # Кнопка "Cancel"
    CANCEL_BTN = (By.XPATH, './/button[@class="btn btn-outline-danger float-right book-room"]')
