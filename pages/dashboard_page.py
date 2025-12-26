from pages.BasePage import BasePage
from utils.logger import Logger


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.dashboard_header = page.locator("(//H6[text()='Dashboard'])")
        self.profile_button = page.locator("(//SPAN[@class='oxd-userdropdown-tab'])//I")
        self.logout_btn = page.locator("(//A[contains(text(),'Logout')])")

    def is_dashboard_visible(self):
        self.logger.info("Checking dashboard page.")
        return self.is_visible(self.dashboard_header)

    def logout(self):
        self.logger.info("Performing logout action")
        self.click(self.profile_button, "Profile Icon")
        self.click(self.logout_btn, "Logout Button")


