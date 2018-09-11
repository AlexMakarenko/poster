from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class SignUpPage(BasePage):
    _PLACE_NAME = '#place_name'
    _COMPANY_TYPE_CAFE_X = "//div[contains(@class, 'company-type')]/button[@data-value=1]"
    _COMPANY_TYPE_STORE_X = "//div[contains(@class, 'company-type')]/button[@data-value=2]"
    _COUNTRY_DROP_DOWN = '#country'
    _NAME_FIELD = '#name'
    _EMAIL_FIELD = '#email'
    _PHONE_FIELD = '#phone'
    _PASSWORD_FIELD = '#password'
    _SUBMIT_BUTTON_X = '//button[contains(@class, "primary")]'

    def enter_place_name(self, place_name: str):
        log.info('Entering place name.')
        return self.se.find(self._PLACE_NAME, wait=True, ttl=DEF_WAIT_TIME).write(place_name)

    def choose_type_company_cafe(self):
        log.info('Choosing type of company is cafe.')
        return self.se.xpath(self._COMPANY_TYPE_CAFE_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def choose_type_company_store(self):
        log.info('Choosing type of company is store.')
        return self.se.xpath(self._COMPANY_TYPE_STORE_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def choose_country(self, country: str):
        log.info('Choosing country.')
        return self.se.find(self._COUNTRY_DROP_DOWN, wait=True, ttl=DEF_WAIT_TIME).select(value=country)

    def enter_name(self, name: str):
        log.info('Entering name.')
        return self.se.find(self._NAME_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(name)

    def enter_email(self, email: str):
        log.info('Entering email.')
        return self.se.find(self._EMAIL_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(email)

    def enter_phone(self, phone: str):
        log.info('Entering phone.')
        return self.se.find(self._PHONE_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(phone)

    def enter_password(self, password: str):
        log.info('Entering password.')
        return self.se.find(self._PASSWORD_FIELD, wait=True, ttl=DEF_WAIT_TIME).write(password)

    def submit_form(self):
        log.info('Submitting form.')
        return self.se.xpath(self._SUBMIT_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()
