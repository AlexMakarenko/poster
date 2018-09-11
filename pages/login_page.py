from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class LoginPage(BasePage):
    _EMAIL_FIELD = '#email'
    _PASSWORD_FIELD = '#password'
    _SUBMIT_BUTTON_X = '//input[@type="submit"]'

    def enter_email(self, email):
        log.info('Entering email.')
        return self.se.find(self._EMAIL_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(email)

    def enter_password(self, password):
        log.info('Entering password.')
        return self.se.find(self._PASSWORD_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(password)

    def click_submit(self):
        log.info('Clicking submit.')
        return self.se.xpath(self._SUBMIT_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
