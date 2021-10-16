# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, browser, url=''):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_add_to_cart_button(self):
        try:
            add_button = self.browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
            return add_button
        except NoSuchElementException as e:
            print('Нет кнопки')

    def add_product_to_cart(self):
        self.should_be_add_to_cart_button().click()

    def should_be_success_message(self):
        try:
            self.browser.find_element_by_css_selector('.alertinner')
        except NoSuchElementException as e:
            print('Нет сообщения ')

    def go_to_writing_review(self):
        link_p = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.ID, "write_review"))
        )
        link_p.click()
        # link_p = self.browser.find_element_by_xpath('//div[@id="reviews"]/following-sibling::p/a')

    def check_that_there_is_name_of_the_goods(self):
        try: self.browser.find_element_by_css_selector \
            ('.col-sm-6.product_main>h1').text
        except NoSuchElementException:
            print('No such text')
            return False

    def check_that_there_is_price_of_the_goods(self):
        try: self.browser.find_element_by_css_selector\
            ('.col-sm-6.product_main>p.price_color').text
        except NoSuchElementException:
            print('No such price')
            return False

    def check_that_there_is_description_of_the_goods(self):
        try: self.browser.find_element_by_css_selector \
            ('.product_page>p:nth-child(3)').text
        except NoSuchElementException:
            print('No such description')
            return False

    def go_back_to_the_main_page(self):
        to_main_page = self.browser.find_element_by_css_selector('.col-sm-7.h1>a')
        to_main_page.click()
        time.sleep(5)
