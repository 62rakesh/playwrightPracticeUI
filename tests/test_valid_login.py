from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data.login_data import LoginData


def test_validLogin(page):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)

    login_page.load("https://opensource-demo.orangehrmlive.com/")
    login_page.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )

    assert dashboard.is_dashboard_visible()
