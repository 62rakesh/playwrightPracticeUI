from pages.configurationPage import module_configuration
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.adminPage import AdminPage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData


def test_select_configuration_submenu(page):
    config = module_configuration(page)
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
    config.navigate_to_selected_submenu()
    config.enable_disable_specific_module("Buzz")

