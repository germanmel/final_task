from .pages.product_page import ProductPage, urls, base_url
from .pages.locators import ProductPageLocators
import time, pytest


#@pytest.mark.parametrize('link', urls)
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
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    



