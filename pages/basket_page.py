import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message not found"

    def should_be_continue_shopping_link_message(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), \
            "Continue shopping link not found"

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product is presented, but should not be"