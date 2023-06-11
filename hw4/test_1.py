import yaml

from BaseApp import BasePage, Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser_name = testdata["browser"]


def test_step1(browser):
    site = BasePage(browser)
    site.go_to_site()

    page = Operations(browser)
    page.enter_username("test")
    page.enter_password("test")
    page.click_login_button()
    assert page.get_error_text() == "401"


def test_step2(browser):
    site = BasePage(browser)
    site.go_to_site()

    page = Operations(browser)
    page.enter_username(testdata["username"])
    page.enter_password(testdata["password"])
    page.click_login_button()

    assert page.get_hello_label() == f'Hello, {testdata["username"]}'
