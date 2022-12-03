from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    """
    Класс для хранения локаторов страницы авторизации в админ-панель
    """

    # Кнопка "Let me hack"
    LET_ME_HACK_BTN = (By.XPATH, './/button[@class="btn btn-primary"]')
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, './/h2[@data-testid="login-header"]')
    # Поле ввода логина
    LOGIN_INPUT = (By.XPATH, './/input[@data-testid="username"]')
    # Поле ввода пароя
    PASSWORD_INPUT = (By.XPATH, './/input[@data-testid="password"]')
    # Кнопка "Login"
    LOGIN_BTN = (By.XPATH, './/button[@data-testid="submit"]')

