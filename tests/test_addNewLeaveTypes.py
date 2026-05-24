import pytest

from pages.leave import LeavePage
from pages.login_page import LoginPage
from test_data.login_data import LoginData
from utils.config_reader import ConfigReader

@pytest.mark.leave
def test_add_newLeaveTypes(page):
    login = LoginPage(page)
    login.load(ConfigReader.get_base_url())
    login.login(
        LoginData.valid_user["username"],
        LoginData.valid_user["password"]
    )
    leave = LeavePage(page)
    leave.navigate_to_leave_page()
    leave.if_leave_page_is_visible()
    leave.click_on_leave_types()
    leave.click_on_add_newLeaveTypes()
    leave.enter_new_leaveType_name("IN - vacation LEAVE")
    leave.verify_if_new_leaveType_is_added("IN - vacation LEAVE")


