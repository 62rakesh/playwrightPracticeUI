from pages.BasePage import BasePage
from utils.assertions import Assertions


class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.admin_menu = page.locator("(//span[normalize-space()='Admin'])")
        self.addUser_button = page.locator("(//DIV[@class='orangehrm-header-container'])//BUTTON")
        self.deleteBtn = page.locator("//I[@class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.delete_text = page.locator("div.orangehrm-text-center-align")
        self.yes_delete = page.locator("//I[@class='oxd-icon bi-trash oxd-button-icon']")

    def click_on_admin_menu(self):
        self.logger.info("Performing Admin functionality test")
        self.click(self.admin_menu, "Admin menu")

    def is_admin_page_visible(self):
        Assertions.assert_visible(self.addUser_button, "Admin page is not visible")

    def select_user_checkbox_by_employee_name(self, emp_name: str):
        self.logger.info("select a specific user from the user table")
        table_body = self.page.locator(".oxd-table-body")

        last_scroll_top = -1

        while True:
            rows = table_body.locator("div[role='row']").all()

            for row in rows:
                record_count = row.locator(f"text={emp_name}").count()
                if record_count > 0:
                    self.logger.info(f"{record_count}:matching employee name found from the table")
                    checkbox = row.locator("input[type='checkbox']")

                    # DOM-level click (bypasses Playwright auto-scroll)
                    checkbox.evaluate("el => el.click()")
                    self.logger.info("click on the selected user checkbox")
                    return

            # Manual scroll
            current_scroll_top = table_body.evaluate("el => el.scrollTop")

            if current_scroll_top == last_scroll_top:
                break  # reached end

            last_scroll_top = current_scroll_top

            table_body.evaluate("el => el.scrollTop += 300")
            self.page.wait_for_timeout(1000)
        raise Exception(f"Employee '{emp_name}' not found")

    def delete_selected_user(self):
        self.logger.info("Delete the selected employee")
        self.click(self.deleteBtn, "Delete selected user")
        Assertions.assert_text(self.delete_text, "The selected record will be permanently deleted. Are you sure you want to continue?")
        self.logger.info(f"Expected text:'{self.delete_text.text_content()}'")
        self.click(self.yes_delete, "Yes,Delete")
        self.logger.info("User deleted the selected employee")




