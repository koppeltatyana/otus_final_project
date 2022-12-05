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
