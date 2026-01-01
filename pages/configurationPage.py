from pages.BasePage import BasePage


class module_configuration(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.configuration = page.locator("(//SPAN[contains(text(),'Configuration ')])")
        self.submenu = page.locator("//A[@class='oxd-topbar-body-nav-tab-link']")
        self.row = page.locator("(//DIV[@class='orangehrm-module-field-row'])")
        self.modules = page.locator("(//P[@class='oxd-text oxd-text--p orangehrm-module-field-label'])")
        self.toggle_button = page.locator("(//INPUT[@type='checkbox'])")
        self.save_button = page.locator("button.oxd-button")

    def navigate_to_selected_submenu(self):
        self.logger.info("Resetting modules")
        self.click(self.configuration, "configuration menu")
        self.logger.info("user clicked on the configuration menu")
        sub_menu_count = self.submenu.count()
        self.logger.info(f"Total submenus are: {sub_menu_count}")
        for i in range(sub_menu_count):
            item = self.submenu.nth(i)
            text = item.inner_text().strip()
            self.logger.info(f"submenus:{text}")

            if text == "Modules":
                item.click()
                self.logger.info(f"submenu: {text}: is selected")
                break

    def enable_disable_specific_module(self, module_name):
        self.logger.info("Enable or disable module")
        row_count = self.row.count()
        for i in range(row_count):
            row = self.row.nth(i)
            self.logger.info(f"Total modules:{row_count}")
            label = row.locator(
                "p.orangehrm-module-field-label"
            ).inner_text().strip()
            self.logger.info(f"modules found:{label}")
            if label == module_name:
                toggle_ui = row.locator("span.oxd-switch-input")
                toggle_ui.click()
                self.click(self.save_button, "save button")
                self.logger.info(f"module: '{module_name}' is updated successfully.")
                break

                # return

        # raise Exception(f"Module '{module_name}' is not found!")



