from.pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    # Забираеи цену и название на ПДП
    page.attributes_on_product_page()
    # Добавляем товар в корзинку 
    page.go_to_product_page()
    # Решаем квиз
    page.solve_quiz_and_get_code()
    # Проверяем ОР
    page.attributes_in_basket_messages()
    