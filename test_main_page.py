import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# тест поддерживает выбор браузера
def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)  # для проверки языка
    browser.implicitly_wait(1)
    assert browser.find_element_by_css_selector("#add_to_basket_form button"), "something wrong with button"
    browser.quit()
