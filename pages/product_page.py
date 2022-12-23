from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
     
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()
              
    def attributes_in_basket_messages(self):
        name_point = self.browser.find_element(*ProductPageLocators.NAME_LINE).text
        price_point = self.browser.find_element(*ProductPageLocators.PRICE_LINE).text
        compare_name_point = self.browser.find_element(*ProductPageLocators.COMPARE_NAME_POINT).text
        compare_price_point = self.browser.find_element(*ProductPageLocators.COMPARE_PRICE_POINT).text
        assert name_point == compare_name_point, "That is not ordered"
        assert price_point == compare_price_point, "Basket price is incorrect" 
        print(name_point)
        print(price_point)
        print("***")
        print(compare_name_point)
        print(compare_price_point)