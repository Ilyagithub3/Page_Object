from .locators import ProductAddBasket
from .base_page import BasePage

class ProductBasket(BasePage):
    def should_be_product_basket(self):
        self.add_basket()
        self.should_be_product_added_to_basket()
        self.should_be_basket_total_equal_to_product_price()
    def add_basket(self):
        basket_add = self.browser.find_element(*ProductAddBasket.BUTTON_ADD_BASKET)
        basket_add.click()
        self.solve_quiz_and_get_code()

    def should_be_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductAddBasket.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductAddBasket.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, "Product name in message doesn't match"

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductAddBasket.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductAddBasket.BASKET_TOTAL).text
        assert product_price == basket_total, "Basket total doesn't match product price"
