from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open() 
    # Добавляем товар в корзину 
    page.go_to_product_page()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is an element"

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There an element"

def test_message_disappeared_after_adding_product_to_basket(browser): 
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open() 
    # Добавляем товар в корзину
    page.go_to_product_page()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Absolutely NO" 

    # вынести ассерты отсюда к х**м