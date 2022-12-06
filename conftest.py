from _pytest.fixtures import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.helpers import get_settings


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
    parser.addoption('--remote', action='store_true', help='Enter "--remote" if you want to execute remote server')
    parser.addoption('--executor', default='192.168.0.103:4444/wd/hub', help='Enter executor url for remote run')
    parser.addoption(
        '--enable_vnc',
        action='store_true',
        help='Enter "--enable_vnc" if you want to see browser during the test'
    )
    parser.addoption(
        '--enable_video',
        action='store_true',
        help='Enter "--enable_video" if you want record the video during the test'
    )
    parser.addoption(
        '--enable_selenoid_logs',
        action='store_true',
        help='Please, enter "--enable_selenoid_logs" if you want to record logs during the test'
    )


@fixture(scope='function')
def browser(request):
    setting_config = get_settings()

    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')
    is_remote = request.config.getoption('--remote')
    executor = request.config.getoption('--executor')
    enable_vnc = request.config.getoption('--enable_vnc')
    enable_video = request.config.getoption('--enable_video')
    enable_selenoid_logs = request.config.getoption('--enable_selenoid_logs')

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
        # capabilities = {}
        capabilities = {
            'browserName': browser_name,
            'version': '107.0',
            'name': 'Tatyana',
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'selenoid:options': {
                'enableVNC': enable_vnc,
                'enableVideo': enable_video,
                'enableLogs': enable_selenoid_logs,
            }
        }
        driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=capabilities,
            options=options,
        )
    else:
        if browser_name == 'chrome':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser_name == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        else:
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)

    def fin():
        driver.close()
    request.addfinalizer(fin)

    driver.set_window_size(setting_config['BROWSER_WINDOW_WIDTH'], setting_config['BROWSER_WINDOW_HEIGHT'])
    driver.base_url = setting_config['SOURCE']['BASE_URL']
    return driver
