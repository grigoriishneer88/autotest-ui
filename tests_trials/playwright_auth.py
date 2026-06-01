from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_field = page.locator('//*[@id=":r0:"]')
    email_field.fill('user.name@gmail.com')
    password_field = page.locator('//*[@id=":r1:"]')
    password_field.fill('password')
    login_button = page.locator('//*[@id="login-page-login-button"]')
    login_button.click()
    wrong_email_or_password = page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]')
    expect(wrong_email_or_password).to_be_visible()
    expect(wrong_email_or_password).to_have_text("Wrong email or password")

    page.wait_for_timeout(1000)


