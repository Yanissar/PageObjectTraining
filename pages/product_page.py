from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    # Добавление товара в корзину со страницы продукта (PDP)
    def add_to_basket_on_pdp(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    # Проверка наименования и стоимости добавленного товара          
    def attributes_in_basket_messages(self):
        name_point = self.browser.find_element(*ProductPageLocators.NAME_LINE).text
        price_point = self.browser.find_element(*ProductPageLocators.PRICE_LINE).text
        compare_name_point = self.browser.find_element(*ProductPageLocators.COMPARE_NAME_POINT).text
        compare_price_point = self.browser.find_element(*ProductPageLocators.COMPARE_PRICE_POINT).text
        assert name_point == compare_name_point, "That is not ordered"
        assert price_point == compare_price_point, "Cart price is incorrect" 

    # Негативная проверка на сообщение об успешном добавлении товара  
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    # Позитивная проверка на сообщение об успешном добавлении тоара  
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented, but should be"
    
    # Проверка на то, что элемент исчез. Внимание! Требуется расскомментировать ожидания
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True