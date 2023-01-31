from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_MESSAGE), "There is no message about an empty basket, it should be."
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_TOTAL), "There are products in basket, it should be empty."
