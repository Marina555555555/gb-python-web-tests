import yaml

from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

url = "https://test-stand.gb.ru"
site = Site(f"{testdata['address']}/login")


def test_step1(username_x_selector, password_x_selector, error_x_selector, btn_selector):
    username_input = site.find_element("xpath", username_x_selector)
    username_input.send_keys("test")
    password_input = site.find_element("xpath", password_x_selector)
    password_input.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", error_x_selector)
    assert err_label.text == "401"


def test_step2(username_x_selector, password_x_selector, hello_x_selector, btn_selector):
    username_input = site.find_element("xpath", username_x_selector)
    username_input.send_keys(testdata["username"])
    password_input = site.find_element("xpath", password_x_selector)
    password_input.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    hello_label = site.find_element("xpath", hello_x_selector)
    assert hello_label.text == f'Hello, {testdata["username"]}'
