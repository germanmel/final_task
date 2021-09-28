from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .locators import BasePageLocators, LoginPageLocators, ProductPageLocators
import pytest

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login page url isn't corrected"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form isn't presented"
    
    def register_new_user(self, email, password):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(email)
        print(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        input_password.send_keys(password)
        print(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        input_password2.send_keys(password)
        print(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
