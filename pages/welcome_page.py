from config import DEF_WAIT_TIME
from pages import BasePage


class WelcomePage(BasePage):
    _CONTINUE_BUTTON_X = '//button[contains(@class, "btn-green")]'

    def click_continue(self):
        return self.se.xpath(self._CONTINUE_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
