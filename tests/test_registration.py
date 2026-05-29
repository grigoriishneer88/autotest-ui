from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email_field = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        name_field = chromium_page.get_by_test_id("registration-form-username-input").locator('input')
        password_field = chromium_page.get_by_test_id("registration-form-password-input").locator('input')
        registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        email_field.fill("test2@test.com")
        name_field.fill("test2")
        password_field.fill("test2")
        registration_button.click()
        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()

@pytest.mark.regression
@pytest.mark.authorisation
def test_wrong_email_or_password(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_field = chromium_page.locator('//*[@id=":r0:"]')
    email_field.fill('user.name@gmail.com')
    password_field = chromium_page.locator('//*[@id=":r1:"]')
    password_field.fill('password')
    login_button = chromium_page.locator('//*[@id="login-page-login-button"]')
    login_button.click()
    wrong_email_or_password = chromium_page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]')
    expect(wrong_email_or_password).to_be_visible()
    expect(wrong_email_or_password).to_have_text("Wrong email or password")



