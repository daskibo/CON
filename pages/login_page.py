from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present (*LoginPageLocators.LOGIN_LINK), "Login url is not presented"
        login_link = self.browser.find_element (*LoginPageLocators.LOGIN_LINK)
        login_link.click ()
        assert 'login' in self.browser.current_url , f"There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM_LINK), "Registration form is not presented"# реализуйте проверку, что есть форма регистрации на странице

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_submit.click()
