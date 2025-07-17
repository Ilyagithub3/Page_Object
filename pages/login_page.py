from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login not found in url"

    def should_be_login_form(self):
        assert self.is_elemnt_present(*LoginPageLocators.FORMA_LOGIN), "Form login not found"

    def should_be_register_form(self):
        assert self.is_elemnt_present(*LoginPageLocators.FORMA_REGISTR), "Form register not found"