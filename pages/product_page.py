from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Can't find the add_button"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        basket_button.click()

    def basket_price_equals_book_price(self):
        book_price_founder = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price_founder.text
        basket_price_founder = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price = basket_price_founder.text
        assert book_price == basket_price, "Prices of basket and book should be equals"

    def book_names_are_equal(self):
        book_name_founder = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_the_basket_founder = self.browser.find_element(*ProductPageLocators.BOOK_IN_THE_BASKET_NAME)
        book_name = book_name_founder.text
        book_name_in_the_basket = book_name_in_the_basket_founder.text
        assert book_name == book_name_in_the_basket

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_disappeard(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
