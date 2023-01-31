from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
