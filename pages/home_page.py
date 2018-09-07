from config import HOME_PAGE, DEF_WAIT_TIME
from pages import BasePage


class HomePage(BasePage):
    _TRY_FOR_FREE_BUTTON_X = '//a[@href="/signup"]/button'
    _LOGIN_BUTTON_X = '//button[@class="login"]'

    def open_home_page(self):
        return self.open_page(HOME_PAGE)

    def click_try_for_free_button(self):
        return self.se.xpath(self._TRY_FOR_FREE_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def click_login(self):
        return self.se.xpath(self._LOGIN_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
