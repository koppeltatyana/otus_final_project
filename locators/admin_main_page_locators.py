from selenium.webdriver.common.by import By


class AdminMainPageLocators:
    """
    Класс для хранения локаторов главной странице админ-панели
    """

    # -------------------------------------------------- БЛОК ХЕДЕРА ------------------------------------------------- #
    # Кнопка "Logout"
    LOGOUT_BTN = (By.XPATH, './/li/a[@class="nav-link" and text()="Logout"]')

    # -------------------------------------------- БЛОК СУЩЕСТВУЮЩИХ НОМЕРОВ ----------------------------------------- #
    # Элемент с информацией по номеру
    ROOM_ITEM = (By.XPATH, './/div[@data-testid="roomlisting"]')
    # Поле с номером комнаты
    ROOM_NUMBER = (By.XPATH, './/div[@class="col-sm-1"][1]/p')
    # Поле с типом комнаты
    ROOM_TYPE = (By.XPATH, './/div[@class="col-sm-2"][1]/p')
    # Поле с доступностью комнаты
    ROOM_ACCESSIBLE = (By.XPATH, './/div[@class="col-sm-2"][2]/p')
    # Поле со стоимостью комнаты
    ROOM_PRICE = (By.XPATH, './/div[@class="col-sm-1"][2]/p')
    # Поле с деталями комнаты
    ROOM_DETAILS = (By.XPATH, './/div[@class="col-sm-5"][1]/p')
    # Иконка удаления комнаты
    ROOM_DELETE_BTN = (By.XPATH, './/span[@class="fa fa-remove roomDelete"]')

    # -------------------------------------------- БЛОК ДЛЯ СОЗДАНИЯ НОМЕРОВ ----------------------------------------- #
    # Поле ввода номера комнаты
    ROOM_NUMBER_FIELD = (By.ID, 'roomName')
    # Поле ввода типа комнаты
    ROOM_TYPE_FIELD = (By.ID, 'type')
    # Поле ввода доступности комнаты
    ROOM_ACCESSIBLE_FIELD = (By.ID, 'accessible')
    # Поле ввода стоимости комнаты
    ROOM_PRICE_FIELD = (By.ID, 'roomPrice')
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
    # Кнопка "Create"
    CREATE_BTN = (By.ID, 'createRoom')
