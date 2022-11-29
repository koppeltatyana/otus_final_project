import logging
import os
from datetime import datetime

from _pytest.config import hookimpl
from _pytest.fixtures import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.helpers import get_settings


@hookimpl(tryfirst=True)
def pytest_sessionstart():
    log_dir = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)


pytest_plugins = [
    'fixtures.ui',
    'fixtures.api'
  ]


def pytest_addoption(parser):
    parser.addoption('--browser_name', default='chrome', help='Choose correct browser name.')
    parser.addoption(
        '--headless',
        action='store_true',
        help='Enter "--headless" option if you don\'t want to see browser during a test'
    )
    parser.addoption('--mobile', action='store_true', help='Enter "--mobile" if you want to start mobile test version')
    parser.addoption('--remote', action='store_true', help='Enter "--remote" if you want to execute remote server')


@fixture(scope='function')
def browser(request):
    setting_config = get_settings()

    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')
    is_remote = request.config.getoption('--remote')

    if browser_name not in ['chrome', 'firefox', 'edge', 'MicrosoftEdge']:
        raise AssertionError('This browser is not supported.')

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        options = webdriver.EdgeOptions()

    if is_remote:
        driver = ''
    else:
        if browser_name == 'chrome':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser_name == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        else:
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)

    # инициализация логгера
    logger = init_logger('INFO', request)
    logger.info(f'Browser was started at {datetime.now()}')

    def fin():
        driver.close()
        logger.info(f'Browser was closed at {datetime.now()}')

    request.addfinalizer(fin)

    driver.set_window_size(setting_config['BROWSER_WINDOW_WIDTH'], setting_config['BROWSER_WINDOW_HEIGHT'])
    return driver


def init_logger(log_level, request):
    log_dir = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(log_dir + f'{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    return logger
