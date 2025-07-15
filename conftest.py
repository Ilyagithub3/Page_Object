import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Выбрать браузер: Chrome or Firefox')
    parser.addoption('--language', action='store', default=None,
                     help='Выбрать язык')
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nСтарт браузера")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print("\nСтарт браузера")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("Неправильное имя браузера")
    yield browser
    print("\nЗакрытие...")
    browser.quit()