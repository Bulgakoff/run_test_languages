import time



link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    print(f'============================= {login_link.text}')
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
    time.sleep(4)
