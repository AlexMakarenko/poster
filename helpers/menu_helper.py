from pages import MenuPage


def open_add_new_supply_page(driver):
    page = MenuPage(driver)
    page.click_on_warehouse_menu_item()
    page.click_on_supply_sub_item()
    page.click_on_add_new_supply()
