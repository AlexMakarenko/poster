from pages import LoginPage, HomePage


def login(driver, email: str, password: str):
    home_page = HomePage(driver)
    page = LoginPage(driver)
    home_page.open_page('https://qa-auto-makarenko.joinposter.com/manage/login')
    page.enter_email(email)
    page.enter_password(password)
    page.click_submit()
