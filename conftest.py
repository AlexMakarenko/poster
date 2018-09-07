import pytest
from config import HEADLESS, CHROMEDRIVER
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    if HEADLESS:
        chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER)
    driver.set_window_size(1920, 1080)
    request.addfinalizer(driver.quit)
    return driver
