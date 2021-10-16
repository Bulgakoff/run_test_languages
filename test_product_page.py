import time

from pj_QA_git_1.product_page import ProductPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

def test_add_to_cart(browser):
    page = ProductPage(browser, link)   # инициализируем объект Page Object
    page.open() # открываем страницу в браузере
    # time.sleep(3)
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину

    page.add_product_to_cart()            # жмем кнопку добавить в корзину

    page.should_be_success_message()      #alertinner   проверяем что есть сообщение с нужным текстом

    page.go_to_writing_review() # write_review перейти к написанию отзыва

    page.check_that_there_is_name_of_the_goods() #проверьте, что есть наименование товара

    page.check_that_there_is_price_of_the_goods() # проверьте, что есть  цена товара

    page.check_that_there_is_description_of_the_goods() # проверьте, что есть описание товара

    page.go_back_to_the_main_page() #  class="col-sm-7 h1"Вернуться на главную страницу