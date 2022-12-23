from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_should_be_empty_negative(self): 
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_DIV), "There is an element, but shouldn't be"

    def basket_should_be_empty_positive(self): 
        assert self.is_element_present(*BasketPageLocators.BASKET_RENEW_SHOPPING), "Basket is not empty"

    def basket_should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "There is no message 'bout empty basket"