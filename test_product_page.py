from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage, base_url, product_link
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
import pytest
from faker import Faker


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.push_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_alert_added_to_cart()
    page.should_be_alert_cart_cost()
    page.check_name_of_book()
    page.check_price()
    

@pytest.mark.skip(reason="not-a-bug")    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.push_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="find out expected result from analytics")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.push_add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_message_should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.show_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.should_be_empty_basket_message()
    cart_page.should_be_continue_shopping_link_message()
    cart_page.should_not_be_goods_in_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        email = fake.email()
        password = fake.password()
        page = ProductPage(browser, base_url)
        page.open()
        log_page = LoginPage(browser, browser.current_url)
        log_page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, base_url)
        page.open()
        page.push_add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_alert_added_to_cart()
        page.should_be_alert_cart_cost()
        page.check_name_of_book()
        page.check_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_url)
        page.open()
        page.should_not_be_success_message()