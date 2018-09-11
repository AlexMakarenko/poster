from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class MenuPage(BasePage):
    _WAREHOUSE_MENU_ITEM_X = '//a[contains(img/@src, "warehouse")]'
    _SUPPLY_SUB_ITEM_X = '//ul[@class="sub-menu"]/li[contains(a/@href, "supply")]'
    _ADD_NEW_SUPPLY_FORM_X = '//body//a[contains(@href, "supply_new/form")]/button'

    def click_on_warehouse_menu_item(self):
        log.info('Clicking on warehouse menu item.')
        return self.se.xpath(self._WAREHOUSE_MENU_ITEM_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def click_on_supply_sub_item(self):
        log.info('Clicking on supply sub item.')
        return self.se.xpath(self._SUPPLY_SUB_ITEM_X, wait=True, ttl=DEF_WAIT_TIME).click()

    def click_on_add_new_supply(self):
        log.info('Clicking on add new supply.')
        return self.se.xpath(self._ADD_NEW_SUPPLY_FORM_X, wait=True, ttl=DEF_WAIT_TIME).click()
