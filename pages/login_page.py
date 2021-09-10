from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        name_register_finder = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM)
        name_register_finder.send_keys("{}".format(email))

        password_register_finder = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM)
        password_register_finder.send_keys("{}".format(password))

        password_second_register_finder = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_AGAIN_FORM)
        password_second_register_finder.send_keys("{}".format(password))

        register_button_finder = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button_finder.click()
