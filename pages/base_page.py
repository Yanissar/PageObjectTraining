import math
from .locators import BasePageLocators
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)
        # заглушено для отрицательных проверок
    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Метод для тестового задания на степик, для понимания архитектуры PO - нафиг не нужен
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    # Метод для отрицательных проверок
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # А это результат нашей оптимизации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_the_basket_from_PDP(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def go_to_the_basket_from_main(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,probably unauthorised user"

    #def fill_register_random(self, email, password):
     #   input_email = self.browser.find_element(*LoginPageLocators.REG_FORM)
      #  input_pass = self.browser.find_element(*LoginPageLocators.PASS_FORM)
       # input_pass2 = self.browser.find_element(*LoginPageLocators.PASS2_FORM)
        #reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        #input_email.send_keys(email)
        #input_pass.send_keys(password)
        #input_pass2.send_keys(password)
       # reg_button.click()
        #assert self.is_element_present(*LoginPageLocators.REG_MESSAGE), "Success registration message is not presented"