from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_book_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_product_added_successfully(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, "Incorrect title of product is added in your basket"
        assert self.is_element_present(
            *ProductPageLocators.ADD_PRODUCT_BASKET_PRICE), "Basket message is not available."
        assert self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, "The price of the product or the basket is incorrect."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADD_PRODUCT_MESSAGE), "Success messages is presented, but should not be"

    def should_success_message_disappears(self):
        assert self.is_disappeared(
            *ProductPageLocators.ADD_PRODUCT_MESSAGE), "Success messages should disappears, but it is not"
