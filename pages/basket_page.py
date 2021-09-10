from .base_page import BasePage
from .locators import BasketPageLocarots


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocarots.BASKET_PRODUCTS)

    def basket_empty_have_text_about(self):
        assert self.is_element_present(*BasketPageLocarots.BASKET_IS_EMPTY_TEXT)

