from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_CART_BUTTON = (By.CSS_SELECTOR, ".btn-group")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    PRODUCT_COLOR_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".col-sm-1 p")
    TOTAL_CART_COST = (By.CSS_SELECTOR, ".total:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner a")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    
