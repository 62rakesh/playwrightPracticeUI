import pytest
from pages.login_page import LoginPage
from test_data.login_data import LoginData
from utils.config_reader import ConfigReader


@pytest.mark.parametrize(
    "user", LoginData.invalid_user
)
def test_invalidLogin(page, user):
    login = LoginPage(page)
    # dashboard = DashboardPage(page)

    login.load(ConfigReader.get_base_url())
    login.login(
        user["username"], user["password"]
    )

    assert login.is_error_visible()
    assert "Invalid" in login.get_error_message()
