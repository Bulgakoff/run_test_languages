import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self,  browser, url=''):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_add_to_cart_button(self):
        add_button = self.browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
        print(f'============>>>>{add_button.text}')
        return add_button

    def add_product_to_cart(self):
        self.should_be_add_to_cart_button().click()

    def should_be_success_message(self):
        te = self.browser.find_element_by_css_selector('.alertinner')
        print(te.text)

    def go_to_writing_review(self):
        # button = WebDriverWait(self.browser, 5).until(
        #     EC.element_to_be_clickable((By.ID, "verify"))
        # )
        # button.click()
        link_p = self.browser.find_element_by_xpath('//div[@id="reviews"]/following-sibling::p/a')
        time.sleep(2)
        link_p.click()
        time.sleep(2)

    def check_that_there_is_name_of_the_goods(self):
        pass

    def check_that_there_is_price_of_the_goods(self):
        pass

    def check_that_there_is_description_of_the_goods(self):
        pass

    def go_back_to_the_main_page(self):
        pass
