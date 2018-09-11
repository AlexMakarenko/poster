from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class NewSupplyPage(BasePage):
    _CHOOSE_PRODUCT_DROP_DOWN_X = '//tr//td[@class= "select"]'
    _COUNT_FIELD = '//tbody/tr//input[@name="count"]'
    _COST_FIELD = '//tbody/tr//input[@name="cost"]'
    _SUM_FIELD = '//tbody/tr//input[@name="sum"]'
    _ADD_PRODUCT_BUTTON_X = '//a[contains(@class, "add-ingredient")]'
    _SAVE_BUTTON_X = '//div[contains(@class, "the-submit")]//button'
    _TOTAL_SUM_X = '//div[contains(@class, "total-sum")]/strong'
    _ALERT_X = '//div[contains(@class, "alert")]'

    def open_drop_down_list_of_products(self):
        log.info('Opening drop-down list.')
        return self.se.xpath(self._CHOOSE_PRODUCT_DROP_DOWN_X, wait=True, ttl=DEF_WAIT_TIME).get(-1).click()

    def is_drop_down_list_opened(self):
        log.info('Checking that drop-down list opened.')
        try:
            self.se.xpath('//div[@class="Select-menu-outer"]', wait=True, ttl=2)
        except TimeoutError:
            raise Exception('Drop down list is not opened.')

    def choose_product_from_drop_down_list(self, product: str):
        log.info('Choosing product from drop-down list.')
        xpath = '//div[@class="Select-menu"]//div[contains(span//text(), "{}")]'.format(product)
        return self.se.xpath(xpath, wait=True, ttl=DEF_WAIT_TIME).click()

    def enter_count(self, amount):
        log.info('Entering count of the product.')
        return self.se.xpath(self._COUNT_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).clear().write(amount)

    def enter_cost(self, cost):
        log.info('Entering cost of the product.')
        return self.se.xpath(self._COST_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).clear().write(cost)

    def get_sum_value(self):
        log.info('Getting sum value.')
        return self.se.xpath(self._SUM_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).value()

    def click_add_new_product(self):
        log.info('Clicking add new product.')
        return self.se.xpath(self._ADD_PRODUCT_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def click_save(self):
        log.info('Clicking save.')
        return self.se.xpath(self._SAVE_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def get_total_sum(self):
        log.info('Getting total sum.')
        return self.se.xpath(self._TOTAL_SUM_X, wait=True, ttl=DEF_WAIT_TIME).text()

    def is_alert_present(self):
        log.info('Checking is alert present.')
        return True if self.se.xpath(self._ALERT_X) else False

    def check_product_selected(self, name):
        log.info('Checking that product selected.')
        try:
            assert self.se.xpath('//span[@class="product-name"]').get(-1).text() == name
            return True
        except AssertionError:
            return False
