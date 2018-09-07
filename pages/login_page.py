from config import DEF_WAIT_TIME
from pages import BasePage


class LoginPage(BasePage):
    _EMAIL_FIELD = '#email'
    _PASSWORD_FIELD = '#password'
    _SUBMIT_BUTTON_X = '//input[@type="submit"]'

    def enter_email(self, email):
        return self.se.find(self._EMAIL_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(email)

    def enter_password(self, password):
        return self.se.find(self._PASSWORD_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(password)

    def click_submit(self):
        return self.se.xpath(self._SUBMIT_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
