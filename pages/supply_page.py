from config import DEF_WAIT_TIME
from pages import BasePage


class SupplyPage(BasePage):

    def get_total_sum_from_table(self):
        return self.se.xpath('//tr//td[6]', wait=True, ttl=DEF_WAIT_TIME).attribute('title')
