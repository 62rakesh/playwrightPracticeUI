import pytest
import os
import pytest_html
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def page(request, playwright_instance):
    browser_config = ConfigReader.get_browser()

    browser = getattr(playwright_instance, browser_config["name"]).launch(
        headless=browser_config["headless"],
        slow_mo=browser_config["slow_mo"]
    )
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size(
        {"width": 1600, "height": 1080}
    )
    request.node.page = page

    yield page

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            import os
            from datetime import datetime

            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            page.screenshot(path=screenshot_path)


def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = "reports/html"
    os.makedirs(report_dir, exist_ok=True)

    config.option.htmlpath = f"{report_dir}/report_{timestamp}.html"
    config.option.self_contained_html = True
