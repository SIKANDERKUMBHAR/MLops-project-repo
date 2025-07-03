from playwright.sync_api import sync_playwright

def test_ui_prediction():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://@localhost:8000/static/index.html")
        page.fill("#pregnancies", "2")
        page.fill("#glucose", "130")
        page.fill("#bloodpressure", "70")
        page.fill("#bmi", "28.5")
        page.fill("#age", "45")
        page.click("button[type='submit']")
        result = page.text_content("#result")
        assert "Prediction" in result
        browser.close()
