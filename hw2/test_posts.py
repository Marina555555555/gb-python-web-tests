import time

import yaml

from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

url = "https://test-stand.gb.ru"
site = Site(f"{testdata['address']}/login")

def test_create_post(username_x_selector, password_x_selector, hello_x_selector, btn_selector):
    username_input = site.find_element("xpath", username_x_selector)
    username_input.send_keys(testdata["username"])
    password_input = site.find_element("xpath", password_x_selector)
    password_input.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(1)

    hello_label = site.find_element("xpath", hello_x_selector)
    assert hello_label.text == f'Hello, {testdata["username"]}'

    create_btn = site.find_element("xpath", """//*[@id="create-btn"]""")
    create_btn.click()

    time.sleep(1)

    create_post_label = site.find_element("xpath", """//*[@id="app"]/main/div/div/h1""")
    assert create_post_label.text == "Create Post"

    title_input = site.find_element("xpath", """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    title_input.send_keys("NEW TITLE")

    description_input = site.find_element("xpath", """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    description_input.send_keys("NEW DESCRIPTION")

    content_input = site.find_element("xpath", """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    content_input.send_keys("NEW CONTENT")

    save_post_btn = site.find_element("xpath", """//*[@id="create-item"]/div/div/div[7]/div/button""")
    save_post_btn.click()

    time.sleep(1)

    new_post_label = site.find_element("xpath","""//*[@id="app"]/main/div/div[1]/h1""")
    assert new_post_label.text == "NEW TITLE"




