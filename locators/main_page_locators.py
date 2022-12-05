from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Класс для хранения методов по главной странице
    """

    # ------------------------------------------- БЛОК БРОНИРОВАНИЯ НОМЕРОВ ------------------------------------------ #
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

    # ---------------------------------------------- БЛОК ОБРАТНОЙ СВЯЗИ --------------------------------------------- #
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

    # Карта
    MAP = (By.XPATH, './/div[@class="pigeon-overlays"]')
