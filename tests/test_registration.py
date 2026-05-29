from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email_field = page.get_by_test_id("registration-form-email-input").locator('input')
        name_field = page.get_by_test_id("registration-form-username-input").locator('input')
        password_field = page.get_by_test_id("registration-form-password-input").locator('input')
        registration_button = page.get_by_test_id("registration-page-registration-button")
        email_field.fill("test2@test.com")
        name_field.fill("test2")
        password_field.fill("test2")
        registration_button.click()
        context.storage_state(path = 'browser-state.json')
        page.wait_for_timeout(4000)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        page.wait_for_timeout(5000)

@pytest.mark.regression
@pytest.mark.authorisation
def test_wrong_email_or_password():
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



