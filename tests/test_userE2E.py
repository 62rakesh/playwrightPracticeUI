from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData


def test_login_logout_E2E(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.load(ConfigReader.get_base_url())
    login.login(
        LoginData.invalid_cred["username"],
        LoginData.invalid_cred["password"]
    )
    login.is_error_visible()
    login.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )
    dashboard.is_dashboard_visible()
    dashboard.logout()
    login.is_login_page_visible()
