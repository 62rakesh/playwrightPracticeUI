from pages.BasePage import BasePage
import time
from utils.assertions import Assertions

class LeavePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.leave_page = page.locator("(//SPAN[text()='Leave'])")
        self.leave_header = page.locator("(//H6[text()='Leave'])")
        self.configure_btn = page.locator("(//SPAN[text()='Configure '])")
        self.leave_types_btn = page.locator("(//A[text()='Leave Types'])")
        self.add_newLeaveType_btn = page.locator("(//BUTTON[text()=' Add '])")
        self.leave_name = page.locator("(//INPUT[@class='oxd-input oxd-input--active'])[2]")
        self.enter_leaveName = page.locator("(//INPUT[@class='oxd-input oxd-input--focus'])")
        self.save_leaveType_btn = page.locator("(//BUTTON[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[text()=' Save ']")
        self.newly_added_leaveType = page.locator("(//DIV[@class='oxd-table-cell oxd-padding-cell'])//div[text()='CAN - Bereavement']")


    def navigate_to_leave_page(self):
        self.logger.info("Clicked Navigate to LeavePage")
        self.leave_page.click()

    def if_leave_page_is_visible(self):
        Assertions.assert_visible(self.leave_header, "Leave page is not visible")
        self.logger.info("Checked if LeavePage is visible")
        # return self.leave_header.is_visible() and self.configure_btn.is_visible()

    def click_on_leave_types(self):
        self.configure_btn.click()
        self.logger.info("Clicked on Configure menu")
        self.leave_types_btn.click()
        self.logger.info("Clicked on Leave Types menu")

    def click_on_add_newLeaveTypes(self):
        self.logger.info("Clicked on Add New LeaveTypes menu")
        self.add_newLeaveType_btn.click()
        self.logger.info("Clicked on Add New LeaveTypes menu")

    def enter_new_leaveType_name(self, leave_type_name):
        self.logger.info(f"The new leave type name is: {leave_type_name}")
        self.leave_name.click()
        self.enter_leaveName.fill(leave_type_name)
        self.logger.info("clicked on save button")
        self.save_leaveType_btn.click()
        time.sleep(7)

    def verify_if_new_leaveType_is_added(self, new_leave_type_name):
        self.logger.info("Verifying if new leave type is added")
        new_leave_type_locator = self.page.locator(f"(//DIV[@class='oxd-table-cell oxd-padding-cell'])//div[text()='{new_leave_type_name}']")
        self.logger.info(f"A new leave type: {new_leave_type_name} is added successfully.")
        Assertions.assert_visible(new_leave_type_locator, f"New leave type '{new_leave_type_name}' is not added successfully.")




