from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()