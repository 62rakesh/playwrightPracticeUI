import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
@pytest.mark.logout
def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.load(ConfigReader.get_base_url())
    login.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )
    dashboard.is_dashboard_visible()
    dashboard.logout()

    login.is_login_page_visible()

