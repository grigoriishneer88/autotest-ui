from playwright.sync_api import Page
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

@pytest.mark.parametrize(
    "email, password, username",  # 1. Имена переменных одной строкой через запятую
    [
        ("test2@test.com", "test2", "test2")
    ]
)
@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.already_signed_in
def test_successful_registration(chromium_page: Page, dashboard_page: DashboardPage, registration_page: RegistrationPage, email:str, username:str, password:str):
        registration_page.visit_registration_page()
        registration_page.registration_form_component.fill_form(email, username, password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()



@pytest.mark.regression
@pytest.mark.authorisation
@pytest.mark.parametrize('email, password', [
    ('email1', 'password'),
    ('email2', 'password1'),
    ('email3', 'password2'),
    ('email4', 'password3'),
])
def test_wrong_email_or_password(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.login_form_component.fill(email, password)
    login_page.login_form_component.check_visible(email, password)
    login_page.click_login_button()
    login_page.check_wrong_email_or_password_alert()


@pytest.mark.already_signed_in
def test_sign_in(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.dashboard_toolbar_view_component()
