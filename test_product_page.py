from .pages.product_page import ProductPage, urls #product_link
from .pages.locators import ProductPageLocators
import time, pytest


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_alert_added_to_cart()
    page.should_be_alert_cart_cost()
    page.check_name_of_book()
    page.check_price()

  
    



