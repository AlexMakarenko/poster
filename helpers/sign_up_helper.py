from pages import SignUpPage, HomePage
from config import HOME_PAGE, DEF_PASSWORD
from helpers.fake_data_helper import person


def sign_up_account(driver):
    home_page = HomePage(driver)
    home_page.open_page(HOME_PAGE)
    home_page.click_try_for_free_button()
    sign_up_page = SignUpPage(driver)
    sign_up_page.enter_place_name('qa_auto_{}'.format(person.last_name()))
    sign_up_page.choose_country('UA')
    sign_up_page.enter_name(person.name())
    sign_up_page.enter_email(person.email())
    sign_up_page.enter_phone(person.telephone(mask='##########'))
    sign_up_page.enter_password(DEF_PASSWORD)
    sign_up_page.submit_form()
