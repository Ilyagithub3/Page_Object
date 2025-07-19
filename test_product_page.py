import pytest
from .pages.product_page import ProductBasket
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


@pytest.mark.basket
class TestBasket():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductBasket(browser, link)
        page.open()
        page.should_be_login_link()
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductBasket(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products()
        basket_page.should_be_empty_basket_message()

@pytest.mark.registr
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductBasket(browser, link)  # Инициализация страницы
        page.open()  # Открываем страницу (это вызовет browser.get())
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductBasket(browser, link)
        page.open()
        page.should_be_product_basket()