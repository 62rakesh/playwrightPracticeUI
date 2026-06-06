import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData

@pytest.mark.login
def test_validLogin(page):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    # login_page.load("https://opensource-demo.orangehrmlive.com/")
    login_page.load(ConfigReader.get_base_url(),ConfigReader.load_env_config())
    login_page.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )

    dashboard.is_dashboard_visible()
