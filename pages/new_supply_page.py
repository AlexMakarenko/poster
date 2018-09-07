from config import DEF_WAIT_TIME
from pages import BasePage


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
        return self.se.xpath(self._CHOOSE_PRODUCT_DROP_DOWN_X, wait=True, ttl=DEF_WAIT_TIME).get(-1).click()

    def choose_product_in_drop_down_list(self, product: str):
        xpath = '//div[@class="Select-menu-outer"]//span[contains(span/text(), "{}")]'.format(product)
        return self.se.xpath(xpath, wait=True, ttl=DEF_WAIT_TIME).click()

    def enter_count(self, amount):
        return self.se.xpath(self._COUNT_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).clear().write(amount)

    def enter_cost(self, cost):
        return self.se.xpath(self._COST_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).clear().write(cost)

    def get_sum_value(self):
        return self.se.xpath(self._SUM_FIELD, wait=True, ttl=DEF_WAIT_TIME).get(-1).value()

    def click_add_new_product(self):
        return self.se.xpath(self._ADD_PRODUCT_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def click_save(self):
        return self.se.xpath(self._SAVE_BUTTON_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def get_total_sum(self):
        return self.se.xpath(self._TOTAL_SUM_X, wait=True, ttl=DEF_WAIT_TIME).text()

    def is_alert_present(self):
        return True if self.se.xpath(self._ALERT_X) else False

    def check_product_selected(self, name):
        try:
            assert self.se.xpath('//span[@class="product-name"]').get(-1).text() == name
            return True
        except AssertionError:
            return False
