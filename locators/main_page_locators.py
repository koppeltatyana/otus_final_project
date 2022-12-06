from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Класс для хранения методов по главной странице
    """

    # Описание
    DESCRIPTION = (By.XPATH, './/div[@class="col-sm-10"]/p')

    # ---------------------------------------------- БЛОК ДЕТАЛЕЙ НОМЕРОВ -------------------------------------------- #
    # Заголовок блока "Rooms"
    TITLE = (By.XPATH, './/h2[text()="Rooms"]')
    # Элемент номера с описанием и изображением
    ROOM_ITEM = (By.XPATH, './/div[@class="row hotel-room-info"]')
    # Строка с типом номера
    ROOM_TYPE = (By.XPATH, './/div[@class="col-sm-7"]/h3')
    # Строка с описанием номера
    ROOM_DESCRIPTION = (By.XPATH, './/div[@class="col-sm-7"]/p')
    # Строка с деталями номера (искать через find_elements)
    ROOM_DETAILS = (By.XPATH, './/div[@class="col-sm-7"]/ul/li')
    # Кнопка "Booking this room"
    BOOKING_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary float-right openBooking"]')

    # ------------------------------------------- БЛОК БРОНИРОВАНИЯ НОМЕРОВ ------------------------------------------ #
    # Элемент календаря
    CALENDAR_ITEM = (By.XPATH, './/div[@class="rbc-month-view"]')
    # Кнопка с числом на календаре
    CALENDAR_DAY_BTN = (By.XPATH, './/button[text()="{0}"]')
    # Поле ввода имени при бронировании
    BOOKING_FIRSTNAME_INPUT = (By.XPATH, './/input[@class="form-control room-firstname"]')
    # Поле ввода фамилии при бронировании
    BOOKING_LASTNAME_INPUT = (By.XPATH, './/input[@class="form-control room-lastname"]')
    # Поле ввода электронной почты при бронировании
    BOOKING_EMAIL_INPUT = (By.XPATH, './/input[@class="form-control room-email"]')
    # Поле ввода номера телефона при бронировании
    BOOKING_PHONE_INPUT = (By.XPATH, './/input[@class="form-control room-phone"]')
    # Кнопка "Book" при бронировании
    BOOK_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary float-right book-room"]')
    # Сообщение при невозможности бронирования
    ERROR_MSG = (By.XPATH, './/div[@class="alert alert-danger"]')

    # ------------------------------------ МОДАЛЬНОЕ ОКНО УСПЕШНОГО БРОНИРОВАНИЯ ------------------------------------- #
    # Заголовок модального окна "Booking Successful!" после успешного бронирования
    BOOKING_SUCCESSFUL_MODAL_WINDOW_TITLE = (By.XPATH, './/h3[text()="Booking Successful!"]')
    # Кнопка "Close" модального окна "Booking Successful!" после успешного бронирования
    CLOSE_SUCCESSFUL_MODAL_WINDOW_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary" and text()="Close"]')

    # -------------------------------------------- БЛОК ОБРАТНОЙ СВЯЗИ ----------------------------------------------- #
    # Поле ввода имени
    FEEDBACK_NAME_INPUT = (By.XPATH, './/input[@data-testid="ContactName"]')
    # Поле ввода электронной почты
    FEEDBACK_EMAIL_INPUT = (By.XPATH, './/input[@data-testid="ContactEmail"]')
    # Поле ввода номера телефона
    FEEDBACK_PHONE_INPUT = (By.XPATH, './/input[@data-testid="ContactPhone"]')
    # Поле ввода темы письма
    FEEDBACK_SUBJECT_INPUT = (By.XPATH, './/input[@data-testid="ContactSubject"]')
    # Поле ввода сообщения
    FEEDBACK_MESSAGE_INPUT = (By.XPATH, './/textarea[@data-testid="ContactDescription"]')
    # Кнопка "Submit"
    FEEDBACK_SUBMIT_BTN = (By.ID, 'submitContact')

    # Контактное имя
    CONTACT_NAME = (By.XPATH, './/div[@class="col-sm-5"]/p[1]')
    # Контактный адрес
    CONTACT_ADDRESS = (By.XPATH, './/div[@class="col-sm-5"]/p[2]')
    # Контактное имя
    CONTACT_PHONE = (By.XPATH, './/div[@class="col-sm-5"]/p[3]')
    # Контактное имя
    CONTACT_EMAIL = (By.XPATH, './/div[@class="col-sm-5"]/p[4]')

    # Карта
    MAP = (By.XPATH, './/div[@class="pigeon-overlays"]')
