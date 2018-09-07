from copy import deepcopy

from helpers import sign_up_account, add_new_supply, check_supply_created, open_add_new_supply_page, login
from test_data import supply_test_data


def test_add_supply_for_old_user(driver):
    test_data = deepcopy(supply_test_data)
    login(driver, 'otutoso@gmail.com', 'qwerty1')
    open_add_new_supply_page(driver)
    add_new_supply(driver, test_data)
    check_supply_created(driver, test_data)


def test_add_supply_for_new_user(driver):
    test_data = deepcopy(supply_test_data)
    sign_up_account(driver)
    open_add_new_supply_page(driver)
    add_new_supply(driver, test_data)
    check_supply_created(driver, test_data)
