# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case3(self):
        driver = self.driver
        driver.get(
            "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/reviews/add/#addreview")
        try:
            driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
            driver.find_element_by_xpath("//button[@value='Добавить в корзину']").click()
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.XPATH, "//div[@id='messages']/div/div/strong")
            driver.find_element_by_xpath("//div[@id='messages']/div/div/strong").click()
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.ID, "write_review")
            driver.find_element_by_id("write_review").click()
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.XPATH, "//div[@id='content_inner']/article/div/div[2]/h1")
            driver.find_element_by_xpath("//div[@id='content_inner']/article/div/div[2]/h1").click()
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.XPATH, "//div[@id='content_inner']/article/div/div[2]/p")
            driver.find_element_by_xpath("//div[@id='content_inner']/article/div/div[2]/p").click()
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.XPATH, "//div[@id='content_inner']/article/p")
        except Exception as e:
            self.fail("timeout")
        try:
            driver.find_element(By.XPATH, "//div[@id='content_inner']/article/p")
            driver.find_element_by_link_text("Oscar").click()
        except Exception as e:
            self.fail("timeout")

        # def is_element_present(self, how, what):
        #     try:
        #         self.driver.find_element(by=how, value=what)
        #     except NoSuchElementException as e:
        #         return False
        # return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
