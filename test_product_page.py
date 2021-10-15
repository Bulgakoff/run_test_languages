import time

from pj_QA_git_1.product_page import ProductPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

def test_add_to_cart(browser):
    page = ProductPage(browser, link)   # �������������� ������ Page Object
    page.open() # ��������� �������� � ��������
    # time.sleep(3)
    page.should_be_add_to_cart_button()   # ��������� ��� ���� ������ ���������� � �������

    page.add_product_to_cart()            # ���� ������ �������� � �������
    # time.sleep(3)

    page.should_be_success_message()      #alertinner   ��" ��� �������� � ���� �������. "������� ��� ���� ��������� � ������ �������

    page.go_to_writing_review() # id="reviews" ������� � ��������� ������

    page.check_that_there_is_name_of_the_goods() # ���������, ��� ���� ������������ ������
    page.check_that_there_is_price_of_the_goods() # ���������, ��� ����  ���� ������
    page.check_that_there_is_description_of_the_goods() # ���������, ��� ���� �������� ������
    page.go_back_to_the_main_page() # ��������� �� ������� ��������