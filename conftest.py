import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox or safari ")
    parser.addoption('--language', action='store', default="es",
                     help="Choose language: en or fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption ("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options ()
        options.add_experimental_option ('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile ()
        fp.set_preference ("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or safari")
    yield browser
    print("\nquit browser..")
    browser.quit()
