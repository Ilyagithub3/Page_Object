from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocatorsIcon, RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def register_new_user(self, email, password):
        self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(BasePageLocatorsIcon.USER_ICON)
        )