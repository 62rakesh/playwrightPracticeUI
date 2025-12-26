
def test_navigate_to_application(page):
    url = "https://opensource-demo.orangehrmlive.com/"
    page.goto(url, wait_until="domcontentloaded")
    assert "OrangeHRM" in page.title()
