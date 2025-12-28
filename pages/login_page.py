from pages.BasePage import BasePage
from utils.logger import Logger
from utils.assertions import Assertions

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("(//INPUT[@name='username'])")
        self.password_input = page.locator("(//INPUT[@name='password'])")
        self.login_btn = page.locator("(//BUTTON[@type='submit'])")
        self.error_message = page.locator("(//P[text()='Invalid credentials'])")

    def load(self, url):
        self.navigate(url)
        self.is_visible(self.username_input)

    def login(self, username, password):
        self.logger.info("Performing logging action")
        self.fill(self.username_input, username, "Username Input")
        self.fill(self.password_input, password, "Password Input")
        self.click(self.login_btn, "Login Button")
        # print("user logged-in successfully")

    def get_error_message(self):
        print(f"Error message is:{self.get_text(self.error_message)}")
        Assertions.assert_text(self.error_message, "Invalid credentials")
        # self.logger.info("")

        return self.get_text(self.error_message)

    def is_error_visible(self):
        self.logger.info("Checking if error message is visible")
        # return self.is_visible(self.error_message)
        Assertions.assert_visible(self.error_message, "Error message not found!")

    def is_login_page_visible(self):
        Assertions.assert_visible(self.username_input, "Login page not found.")
        # return self.is_visible(self.username_input)
