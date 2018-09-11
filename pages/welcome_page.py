from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class WelcomePage(BasePage):
    _CONTINUE_BUTTON_X = '//button[contains(@class, "btn-green")]'

    def click_continue(self):
        log.info('Clicking on continue on welcome page.')
        return self.se.xpath(self._CONTINUE_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
