from selenium.webdriver.common.by import By


class AdminRoomDetailsPageLocators:
    """
    Класс для хранения локаторов страницы номера админ-панели
    """

    # ----------------------------------------------- СТРАНИЦА ДЕТАЛЕЙ ----------------------------------------------- #
    # Заголовок страницы
    PAGE_TITLE_BY_ROOM_NUMBER = (By.XPATH, './/h2[text()="{0}"]')
    # Кнопка "Edit"
    EDIT_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary float-right" and text()="Edit"]')

    # ---------------------------------------------- БЛОК БРОНИРОВАНИЙ ----------------------------------------------- #
    # Элемент бронирования
    BOOKING_ITEM = (By.XPATH, './/div[@class="detail booking-{0}"]/div[@class="row"]')
    # Имя бронирования
    BOOKING_FIRSTNAME = (By.XPATH, './/div[@class="col-sm-2"][1]/p')
    # Фамилия бронирования
    BOOKING_LASTNAME = (By.XPATH, './/div[@class="col-sm-2"][2]/p')
    # Цена бронирования
    BOOKING_PRICE = (By.XPATH, './/div[@class="col-sm-1"][1]/p')
    # Оплачено ли бронирование
    BOOKING_DEPOSIT_PAID = (By.XPATH, './/div[@class="col-sm-2"][3]/p')
    # Дата заезда
    BOOKING_CHECKIN = (By.XPATH, './/div[@class="col-sm-2"][4]/p')
    # Дата выезда
    BOOKING_CHECKOUT = (By.XPATH, './/div[@class="col-sm-2"][5]/p')
    # Иконка редактирования бронирования по имени пользователя
    BOOKING_EDIT_BTN_BY_FIRSTNAME = (By.XPATH, './/div[@class="col-sm-2"][1]/p/../../div[@class="col-sm-1"][2]/'
                                               'span[@class="fa fa-pencil bookingEdit"]')
    # Иконка удаления бронирования по имени пользователя
    BOOKING_DELETE_BTN_BY_FIRSTNAME = (By.XPATH, './/div[@class="col-sm-2"][1]/p/../../div[@class="col-sm-1"][2]/'
                                                 'span[@class="fa fa-trash bookingDelete"]')

    # -------------------------------------------- СТРАНИЦА РЕДАКТИРОВАНИЯ ------------------------------------------- #
    # Кнопка "Update"
    UPDATE_BTN = (By.XPATH, './/button[@class="btn btn-outline-primary float-right" and text()="Update"]')
    # Кнопка "Cancel"
    CANCEL_BTN = (By.XPATH, './/button[@class="btn btn-outline-danger float-right" and text()="Cancel"]')
    # Поле ввода номера комнаты
    ROOM_NUMBER_FIELD = (By.ID, 'roomName')
    # Поле ввода типа комнаты
    ROOM_TYPE_FIELD = (By.ID, 'type')
    # Поле ввода доступности комнаты
    ROOM_ACCESSIBLE_FIELD = (By.ID, 'accessible')
    # Поле ввода стоимости комнаты
    ROOM_PRICE_FIELD = (By.ID, 'roomPrice')
    # Поле ввода описания комнаты
    ROOM_DESC_FIELD = (By.ID, 'description')
    # Поле ввода ссылки на изображение номера
    ROOM_IMG_FIELD = (By.ID, 'image')
    # Чекбокс "WiFi"
    ROOM_DETAILS_WIFI_CHECKBOX = (By.ID, 'wifiCheckbox')
    # Чекбокс "Refreshments"
    ROOM_DETAILS_REFRESHMENTS_CHECKBOX = (By.ID, 'refreshCheckbox')
    # Чекбокс "TV"
    ROOM_DETAILS_TV_CHECKBOX = (By.ID, 'tvCheckbox')
    # Чекбокс "Safe"
    ROOM_DETAILS_SAFE_CHECKBOX = (By.ID, 'safeCheckbox')
    # Чекбокс "Radio"
    ROOM_DETAILS_RADIO_CHECKBOX = (By.ID, 'radioCheckbox')
    # Чекбокс "Views"
    ROOM_DETAILS_VIEWS_CHECKBOX = (By.ID, 'viewsCheckbox')
