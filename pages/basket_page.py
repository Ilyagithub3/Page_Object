from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_elemnt_present(*BasketLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"