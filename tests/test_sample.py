from utils.logger import Logger


def test_navigate_to_application(page):
    url = "https://opensource-demo.orangehrmlive.com/"
    page.goto(url, wait_until="domcontentloaded")
    print("user navigated to application successfully")
    assert "OrangeHRM" in page.title()
