from time import sleep


def test_test(browser):
    browser.get('https://google.com')
    sleep(4)


def test_api(api_app_key, api_helper):
    a = api_main_info.get_main_info(app_key=api_app_key)
