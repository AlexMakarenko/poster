from config import DEF_WAIT_TIME
from pages import BasePage
from config import log


class SupplyPage(BasePage):

    def get_total_sum_from_table(self):
        log.info('Getting total sum from table.')
        return self.se.xpath('//tr//td[6]', wait=True, ttl=DEF_WAIT_TIME).attribute('title')
