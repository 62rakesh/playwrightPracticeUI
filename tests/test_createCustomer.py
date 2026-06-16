import pytest
from pages.login_page import LoginPage
from pages.timePage import TimePage
from utils.config_reader import ConfigReader
from test_data.login_data import LoginData
from test_data.testdata_generator import TestDataGenerator
from pages.dashboard_page import DashboardPage

@pytest.mark.time
def test_create_customer(page):
    login = LoginPage(page)
    login.load(ConfigReader.get_base_url(), ConfigReader.load_env_config())
    login.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )
    dashboard = DashboardPage(page)
    dashboard.is_dashboard_visible()
    time = TimePage(page)
    time.navigate_to_time_menu()
    time.navigate_to_customer_page()
    customer = TestDataGenerator.addNew_customer()
    time.new_customer(customer)
    time.search_customer(
        customer["customer_name"]
    )
    

