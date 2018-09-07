from time import sleep

from pages import NewSupplyPage, SupplyPage


def add_new_supply(driver, supply_test_data: dict):
    page = NewSupplyPage(driver)
    for key, product in supply_test_data.items():
        page.open_drop_down_list_of_products()
        sleep(0.5)
        page.choose_product_in_drop_down_list(product['name'])
        if not page.check_product_selected(product['name']):
            page.choose_product_in_drop_down_list(product['name'])
        page.enter_count(product['count'])
        page.enter_cost(product['cost'])
        if key != 'product5':
            page.click_add_new_product()
    total_sum = page.get_total_sum()
    supply_test_data.update({'total_sum': ''.join(d for d in total_sum if d in '1234567890.,')})
    page.click_save()


def check_supply_created(driver, supply_test_data: dict):
    page = SupplyPage(driver)
    actual_sum = page.get_total_sum_from_table()
    expected_sum = supply_test_data['total_sum']
    assert expected_sum == actual_sum, 'Wrong total sum. E:{0} A:{1}'.format(expected_sum, actual_sum)
