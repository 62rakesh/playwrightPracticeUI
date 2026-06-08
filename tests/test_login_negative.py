import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


@pytest.mark.parametrize(
    "username,password",
    [
        ("Admin", "wrongpass"),
        ("wrong admin", "Admin123"),
        ("Admin11", "32342312"),
        ("asdasd", "Admin")
    ]
)
def test_invalid_login(page, username, password):
    login = LoginPage(page)
    # login.load("https://opensource-demo.orangehrmlive.com/")
    login.load(ConfigReader.get_base_url(),ConfigReader.load_env_config())
    login.login(username, password)

    login.get_error_message()
    login.is_error_visible()

