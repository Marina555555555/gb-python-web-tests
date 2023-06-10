import requests
import pytest
import yaml


url = 'https://test-stand.gb.ru'
with open("config.yaml") as f:
	config = yaml.safe_load(f)
	username = config["username"]
	password = config["password"]


@pytest.fixture()
def token():
	r = requests.post(f'{url}/gateway/login', data={
		"username": username,
		"password": password,
	})
	return r.json()["token"]


def get_all_posts(token):
	r = requests.get(f'{url}/api/posts', headers={'X-Auth-Token': token}, params={"owner": "notMe"})
	
	return [p["content"] for p in r.json()["data"]]

def get_my_posts(token):
	r = requests.get(f'{url}/api/posts', headers={'X-Auth-Token': token}, params={"owner": "me", "sort": "createdAt", "order": "DESC"})
	
	return [p["content"] for p in r.json()["data"]]


def create_post(token, title, description, content):
	r = requests.post(f'{url}/api/posts', headers={'X-Auth-Token': token}, data={"title": title, "description": description, "content": content})
	assert r.status_code == 200
