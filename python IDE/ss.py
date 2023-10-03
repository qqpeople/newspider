from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://toolwa.com/wooden-fish/")
    page.get_by_role("button", name="已阅").click()
    for i in range(100000):
        page.get_by_role("img", name="muyu").click(click_count=3)
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
