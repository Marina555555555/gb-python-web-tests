import time

import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser_name = testdata["browser"]


class BasePage:
    def __init__(self, driver):
        self.address = "https://test-stand.gb.ru"
        self.driver = driver

    def start_browser(self):
        self.driver.get(self.address)

    def find_element(self, locator, time_to_wait=10):
        time.sleep(0.5)
        return WebDriverWait(self.driver, time_to_wait).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can not find element by locator {locator}")

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.address)


class TestLocators:
    username_x_selector = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    password_x_selector = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    btn_selector = (By.CSS_SELECTOR, """button""")
    error_selector = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    hello_label_selector = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")


    contact_link_selector = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    page_title_selector = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    contact_name_selector = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    contact_email_selector = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    contact_content_selector = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    contact_btn_selector = (By.XPATH, """//*[@id="contact"]/div[4]/button""")

class Operations(BasePage, TestLocators):

    def enter_username(self, username):
        username_input = self.find_element(self.username_x_selector)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(self.password_x_selector)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        btn = self.find_element(self.btn_selector)
        btn.click()

    def get_error_text(self):
        error_label = self.find_element(self.error_selector)
        return error_label.text

    def get_hello_label(self):
        hello_label = self.find_element(self.hello_label_selector)
        return hello_label.text

    def open_contact_form(self):
        contact_link = self.find_element(self.contact_link_selector)
        contact_link.click()

    def get_page_title(self):
        page_title = self.find_element(self.page_title_selector)
        return page_title.text

    def enter_contact_name(self, text):
        username_input = self.find_element(self.contact_name_selector)
        username_input.clear()
        username_input.send_keys(text)

    def enter_contact_email(self, text):
        username_input = self.find_element(self.contact_email_selector)
        username_input.clear()
        username_input.send_keys(text)

    def enter_contact_content(self, text):
        username_input = self.find_element(self.contact_content_selector)
        username_input.clear()
        username_input.send_keys(text)

    def click_contact_btn(self):
        contact_btn = self.find_element(self.contact_btn_selector)
        contact_btn.click()