from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.load("https://opensource-demo.orangehrmlive.com/")
    login.login("Admin", "admin123")

    dashboard.is_dashboard_visible()
    dashboard.logout()

    login.is_login_page_visible()

