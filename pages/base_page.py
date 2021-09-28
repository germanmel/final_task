import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    
    def __init__(self, browser, url, timeout=10): 
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): #открытие страницы
        self.browser.get(self.url)

    def is_element_present(self, how, what): #проверка что элемент существует
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link isn't presented"

    def show_cart_page(self):
        button = self.browser.find_element(*BasePageLocators.SHOW_CART_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self): #математическое решение для нахождения кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def is_not_element_present(self, how, what, timeout=4): #тест упадёт как только увидит искомый элемент
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4): #тест упадёт если элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorized user"
        





