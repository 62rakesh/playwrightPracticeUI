from playwright.sync_api import Locator, Page


class Assertions:

    @staticmethod
    def assert_visible(locator: Locator, message: str):
        assert locator.is_visible(), message

    @staticmethod
    def assert_text(locator: Locator, expected_text: str):
        actual_txt = locator.text_content()
        assert actual_txt == expected_text, (
            f"Expected: {expected_text} but got:{actual_txt}"

        )

    @staticmethod
    def assert_url(page: Page, expected_url: str):
        assert page.url == expected_url, (
            f"Expected:{expected_url} but has got:{page.url}"
        )
