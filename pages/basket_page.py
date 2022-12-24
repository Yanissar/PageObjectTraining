from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # Негативная проверка наполненности корзины  
    def basket_should_be_empty_negative(self): 
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_DIV), "There is an element, but shouldn't be"
    
    # Позитивная проверка наполненности корзины
    def basket_should_be_empty_positive(self): 
        assert self.is_element_present(*BasketPageLocators.BASKET_RENEW_SHOPPING), "Cart is not empty"
    
    # Дополнительная корзинная проверка на сообщение о том, что она пуста
    def basket_should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "There is no message about empty cart"