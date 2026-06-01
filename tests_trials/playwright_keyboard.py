from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_field = page.locator('//*[@id=":r0:"]')
    email_field.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char, delay=300)

    page.keyboard.press("ControlOrMeta+A")
    page.wait_for_timeout(5000)