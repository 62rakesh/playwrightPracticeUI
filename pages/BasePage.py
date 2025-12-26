from playwright.sync_api import Page, Locator
from utils.logger import Logger


class BasePage:

    def __init__(self, page: Page):
        self.page: Page = page
        self.logger = Logger.get_logger(self.__class__.__name__)

    def navigate(self, url):
        self.logger.info(f"Navigating to url: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    # def get_locator(self, selector):
    #     self.logger.info(f"Clicking on element: {selector}")
    #     return self.page.locator(selector)

    def click(self, locator, element_name: str):
        # locator = self.get_locator(locator)
        locator.wait_for(state="visible")
        self.logger.info(f"Clicking on element: {element_name}")
        locator.click()

    def fill(self, locator, value, element_name: str):
        # locator = self.get_locator(selector)
        locator.wait_for(state="visible")
        self.logger.info(f"Entering value into field: {element_name}")
        locator.fill(value)

    def is_visible(self, locator):
        return locator.is_visible()

    def get_text(self, locator):
        # locator = self.get_locator(selector)
        locator.wait_for(state="visible")
        return locator.inner_text()

    def get_title(self):
        return self.page.title()

    def wait_for_text(self, text):
        self.page.wait_for_selector(f"text:{text}")


