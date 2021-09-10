from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, "#register_form [name='registration-email']")
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, "#register_form [name='registration-password1']")
    REGISTER_PASSWORD_AGAIN_FORM = (By.CSS_SELECTOR, "#register_form [name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_page .row .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_page .row h1")
    BOOK_IN_THE_BASKET_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".row .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocarots:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, ".content [id='content_inner'] p")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items .row")
