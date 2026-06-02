from playwright.sync_api import sync_playwright, expect, Page
import pytest

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.already_signed_in
def test_successful_registration(chromium_page: Page, dashboard_page: DashboardPage):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email_field = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        name_field = chromium_page.get_by_test_id("registration-form-username-input").locator('input')
        password_field = chromium_page.get_by_test_id("registration-form-password-input").locator('input')
        registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        email_field.fill("test2@test.com")
        name_field.fill("test2")
        password_field.fill("test2")
        registration_button.click()
        dashboard_page.check_dashboard_title_visibility()



@pytest.mark.regression
@pytest.mark.authorisation
@pytest.mark.parametrize('email, password', [
    ('email1', 'password'),
    ('email2', 'password1'),
    ('email3', 'password2'),
    ('email4', 'password3'),
])
def test_wrong_email_or_password(login_page: LoginPage, email: str, password: str):
    #login_page = LoginPage(page=chromium_page)

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email, password)
    login_page.click_login_button()
    login_page.check_wrong_email_or_password_alert()
    # email_field = chromium_page.locator('//*[@id=":r0:"]')
    # email_field.fill('user.name@gmail.com')
    # password_field = chromium_page.locator('//*[@id=":r1:"]')
    # password_field.fill('password')
    # login_button = chromium_page.locator('//*[@id="login-page-login-button"]')
    # login_button.click()
    # wrong_email_or_password = chromium_page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]')
    # expect(wrong_email_or_password).to_be_visible()
    # expect(wrong_email_or_password).to_have_text("Wrong email or password")

@pytest.mark.already_signed_in
def test_sign_in(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.check_dashboard_title_visibility()
    # chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    # dashboard_title = chromium_page_with_state.get_by_test_id("dashboard-toolbar-title-text")
    # expect(dashboard_title).to_be_visible()
