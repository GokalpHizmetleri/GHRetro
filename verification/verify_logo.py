from playwright.sync_api import sync_playwright, expect
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Navigating to home page...")
        page.goto("http://localhost:8000/", timeout=60000)

        # Verify title
        print(f"Page title: {page.title()}")
        expect(page).to_have_title(re.compile(r"GHRetro"))

        # Verify logo
        logo = page.locator("img[alt='Logo']").first
        if not logo.count():
             logo = page.locator("img[alt='logo']").first

        if logo.count():
            print("Logo found.")
            expect(logo).to_be_visible()
            src = logo.get_attribute("src")
            print(f"Logo src: {src}")
        else:
            print("Logo NOT found via alt text.")

        # Take screenshot
        print("Taking screenshot...")
        page.screenshot(path="/home/jules/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()
