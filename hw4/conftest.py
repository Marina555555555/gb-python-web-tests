import logging

import pytest
import requests
import yaml

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from post import send_mail

url = 'https://test-stand.gb.ru'
with open("testdata.yaml") as f:
	config = yaml.safe_load(f)
	username = config["username"]
	password = config["password"]


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture()
def token():
    logging.info("Logging in")
    try:
        r = requests.post(f'{url}/gateway/login', data={
            "username": username,
            "password": password,
        })
        return r.json()["token"]
    except:
        logging.exception("Error while logging in")

def get_all_posts(token):
    logging.info("Getting all posts")
    try:
        r = requests.get(f'{url}/api/posts', headers={'X-Auth-Token': token}, params={"owner": "notMe"})

        return [p["content"] for p in r.json()["data"]]
    except:
        logging.exception("Error while getting all posts")


def get_my_posts(token):
    try:
        r = requests.get(f'{url}/api/posts', headers={'X-Auth-Token': token},
                         params={"owner": "me", "sort": "createdAt", "order": "DESC"})

        return [p["content"] for p in r.json()["data"]]
    except:
        logging.exception("Error while getting my posts")


def create_post(token, title, description, content):
    try:
        r = requests.post(f'{url}/api/posts', headers={'X-Auth-Token': token},
                          data={"title": title, "description": description, "content": content})
        assert r.status_code == 200
    except:
        logging.exception("Error while creating post")

@pytest.fixture(scope='session', autouse=True)
def send_email_fixture():
    yield
    send_mail()