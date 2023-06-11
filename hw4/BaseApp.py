import time
import logging

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
        try:
            self.driver.get(self.address)
        except:
            logging.exception("Error while opening browser")

    def find_element(self, locator, time_to_wait=10):
        time.sleep(0.5)
        try:
            return WebDriverWait(self.driver, time_to_wait).until(
                expected_conditions.presence_of_element_located(locator),
                message=f"Can not find element by locator {locator}")
        except:
            logging.exception("Element is not found %s", locator)
            return None

    def get_element_property(self, locator, property):
        try:
            element = self.find_element(locator)
            return element.value_of_css_property(property)
        except:
            logging.exception("Property %s is not found of %s", property, locator)

    def go_to_site(self):
        return self.driver.get(self.address)


class TestLocators:
    ids = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)

        for key, value in locators['xpath'].items():
            ids[key] = (By.XPATH, value)
        for key, value in locators['css'].items():
            ids[key] = (By.CSS_SELECTOR, value)


class Operations(BasePage, TestLocators):

    def enter_username(self, username):
        logging.info("Entering username %s", username)
        username_input = self.find_element(self.ids["username_selector"])
        if not username_input:
            logging.error("Username input is not found")
        else:
            username_input.clear()
            username_input.send_keys(username)

    def enter_password(self, password):
        logging.info("Entering password %s", password)
        password_input = self.find_element(self.ids["password_selector"])
        if not password_input:
            logging.error("Password input is not found")
        else:
            password_input.clear()
            password_input.send_keys(password)

    def click_login_button(self):
        logging.info("Clicking button")
        btn = self.find_element(self.ids["btn_selector"])
        if not btn:
            logging.error("Button is not found")
        else:
            btn.click()

    def get_error_text(self):
        logging.info("Getting error text")
        error_label = self.find_element(self.ids["error_selector"])
        if not error_label:
            logging.error("Error label is not found")
        else:
            return error_label.text

    def get_hello_label(self):
        logging.info("Getting hello text")
        hello_label = self.find_element(self.ids["hello_label_selector"])
        if not hello_label:
            logging.error("Hello label is not found")
        else:
            return hello_label.text

    def open_contact_form(self):
        logging.info("Open contact form")
        contact_link = self.find_element(self.ids["contact_link_selector"])
        if not contact_link:
            logging.error("Contact link is not found")
        else:
            contact_link.click()

    def get_page_title(self):
        logging.info("Getting page title")
        page_title = self.find_element(self.ids["page_title_selector"])
        if not page_title:
            logging.error("Page title is not found")
        else:
            return page_title.text

    def enter_contact_name(self, text):
        logging.info("Entering contact name %s", text)
        input = self.find_element(self.ids["contact_name_selector"])
        if not input:
            logging.error("Name input is not found")
        else:
            input.clear()
            input.send_keys(text)

    def enter_contact_email(self, text):
        logging.info("Entering contact email %s", text)
        input = self.find_element(self.ids["contact_email_selector"])
        if not input:
            logging.error("Email input is not found")
        else:
            input.clear()
            input.send_keys(text)

    def enter_contact_content(self, text):
        logging.info("Entering contact content %s", text)
        input = self.find_element(self.ids["contact_content_selector"])
        if not input:
            logging.error("Content input is not found")
        else:
            input.clear()
            input.send_keys(text)

    def click_contact_btn(self):
        logging.info("Clicking contact button")
        contact_btn = self.find_element(self.ids["contact_btn_selector"])
        if not contact_btn:
            logging.error("Contact button is not found")
        else:
            contact_btn.click()