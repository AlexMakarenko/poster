from elementium.drivers.se import SeElements
from selenium.webdriver.support.ui import WebDriverWait
from config import log


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.se = SeElements(browser=self.driver)
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self, url: str):
        log.info('Opening page: {}'.format(url))
        self.se.navigate(url)



