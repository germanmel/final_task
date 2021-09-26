import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1" #базовая ссылка 
urls = [f"{base_url}{promo_number}" for promo_number in range(1)] #создаём список url меняя последюю цифру циклом
#urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail) #маркируем url седьмой ссылки как xfail

class ProductPage(BasePage):
    
    def should_be_alert_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT_ADDED_TO_CART), "Alert added to cart not found"

    def should_be_alert_cart_cost(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE), "Alert with cart cost not found"

    def push_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def check_name_of_book(self):
        alert_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT_ADDED_TO_CART)
        alert_name = alert_name.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        self.show_cart_page()
        product_name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART)
        product_name_cart = product_name_cart.text
        print(alert_name, product_name, product_name_cart)
        assert product_name == alert_name, "Name of book on product page differs from name in alert"
        assert product_name_cart == alert_name, "Name of book in cart differs from name in alert"

    def check_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART)
        product_price = product_price.text
        cart_cost = self.browser.find_element(*ProductPageLocators.TOTAL_CART_COST)
        cart_cost = cart_cost.text
        print(product_price, cart_cost)
        assert product_price == cart_cost, "Cart cost isn't equal product price"

    def should_not_be_success_message(self): #тест упадёт как только увидит искомый элемент
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    

        
