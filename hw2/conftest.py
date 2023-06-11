import pytest

@pytest.fixture()
def username_x_selector():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def password_x_selector():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def error_x_selector():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def hello_x_selector():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def btn_selector():
    return """button"""