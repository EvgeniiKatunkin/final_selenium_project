from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import time


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_in_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
