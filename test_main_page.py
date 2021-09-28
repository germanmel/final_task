from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage #login_link
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

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.show_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.should_be_empty_basket_message()
    cart_page.should_be_continue_shopping_link_message()
    cart_page.should_not_be_goods_in_basket()

    


