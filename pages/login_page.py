from mimesis import Person
from .base_page import BasePage
from .locators import LoginPageLocators
from mimesis.locales import Locale
person = Person(Locale.EN)

class LoginPage(BasePage):

    # Двойная проверка на корректность перехода
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
    
    # Проверка на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no /login/ in URL"
    
    # Проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login input form is not presented"
    
    # Проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
         assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration input form is not presented"
    
    # Регистрируем нового пользователя
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REG_FORM)
        input_pass = self.browser.find_element(*LoginPageLocators.PASS_FORM)
        input_pass2 = self.browser.find_element(*LoginPageLocators.PASS2_FORM)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        input_email.send_keys(email)
        input_pass.send_keys(password)
        input_pass2.send_keys(password)
        reg_button.click()
        assert self.is_element_present(*LoginPageLocators.REG_MESSAGE), "Success registration message is not presented"