from .pages.login_page import LoginPage, login_link
from .pages.main_page import MainPage, link

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def should_be_login_page(browser):
    page = LoginPage(browser,login_link)
    page.open()
    page.should_be_login_page()


def test_login_url_is_correct(browser):
    page = LoginPage(browser,login_link)
    page.open()
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser,login_link)
    page.open()
    page.should_be_login_form()

def test_guest_should_be_register_form(browser):
    page = LoginPage(browser,login_link)
    page.open()
    page.should_be_register_form()


    


