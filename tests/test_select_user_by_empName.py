from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.adminPage import AdminPage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData


def test_select_user_by_empName(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    admin_page = AdminPage(page)

    login_page.load(ConfigReader.get_base_url())
    login_page.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )

    dashboard_page.is_dashboard_visible()
    admin_page.click_on_admin_menu()
    admin_page.is_admin_page_visible()
    admin_page.select_user_checkbox_by_employee_name("jumanji thunder")
    admin_page.delete_selected_user()
    dashboard_page.logout()
