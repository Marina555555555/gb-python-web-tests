import time

import yaml

from hw3.BaseApp import BasePage, Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

url = "https://test-stand.gb.ru"

def test_contact(browser):
    site = BasePage(browser)
    site.go_to_site()

    # Login
    page = Operations(browser)
    page.enter_username(testdata["username"])
    page.enter_password(testdata["password"])
    page.click_login_button()

    time.sleep(1)

    assert page.get_hello_label() == f'Hello, {testdata["username"]}'

    # Open contact form
    page.open_contact_form()
    assert page.get_page_title() == "Contact us!"

    page.enter_contact_name("NAME")
    page.enter_contact_email("my@email.com")
    page.enter_contact_content("CONTENT")
    page.click_contact_btn()
    time.sleep(1)

    alert = page.driver.switch_to.alert
    assert alert.text == "Form successfully submitted"
    alert.accept()
