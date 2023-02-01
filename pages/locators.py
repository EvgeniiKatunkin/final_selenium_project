from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRMATION = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TOTAL = (By.ID, "basket_totals")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
