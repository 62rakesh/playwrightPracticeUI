import time

from pages.BasePage import BasePage
from test_data.testdata_generator import TestDataGenerator


class TimePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.time_menu = page.locator("(//SPAN[text()='Time'])")
        self.project_info = page.locator("(//SPAN[contains(text(),'Project Info ')])")
        self.customers = page.locator("(//A[contains(text(),'Customers')])")
        self.customer_name = page.locator("(//DIV[@class='oxd-input-group oxd-input-field-bottom-space'])//INPUT")
        self.save_customer = page.locator("(//BUTTON[text()=' Save '])")
        self.add_customer_btn = page.locator("(//BUTTON[text()=' Add '])")
        self.project_menu = self.page.locator("(//A[text()='Projects'])")
        self.customer_name_hint = self.page.locator("(//INPUT[@placeholder='Type for hints...'])[1]")
        self.select_customer = self.page.locator("(//DIV[@class='oxd-autocomplete-option --selected'])//SPAN")
    def navigate_to_time_menu(self):
        self.logger.info("click_on_time_menu")
        self.click(self.time_menu, "Time")
        self.is_visible(self.project_info)
        self.logger.info("Check if project-info is visible")

    def navigate_to_customer_page(self):
        self.logger.info("create_customer")
        self.click(self.project_info,"project-info")
        self.click(self.customers, "Customer")
        self.logger.info("Add new customer page")
        self.click(self.add_customer_btn, "Add Customer")
        self.customer_name.click()

    def new_customer(self,new_customer):
        # new_customer = TestDataGenerator.addNew_customer()
        self.customer_name.fill(
            new_customer["customer_name"]
        )
        self.save_customer.click()
        time.sleep(5)
        self.logger.info(f"Customer:{new_customer} is created")

    def search_customer(self, cus):
        self.logger.info(f"search_customer")
        self.project_info.click()
        self.project_menu.click()
        self.logger.info("user navigates to the project page")
        self.customer_name_hint.click()
        self.customer_name_hint.fill(cus)
        time.sleep(3)
        self.logger.info(f"Customer:{cus} is searched successfully")
        # self.page.locator(f"(//DIV[@class='oxd-autocomplete-option'])//SPAN[text()='{cus}']").click()
        self.page.get_by_role("option", name=cus).click()








