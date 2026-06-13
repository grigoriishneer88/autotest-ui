from playwright.sync_api import Page
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.already_signed_in
class TestAuthorisation:
    @pytest.mark.regression
    @pytest.mark.authorisation
    @pytest.mark.parametrize('email, password', [
        ('email1', 'password'),
        ('email2', 'password1'),
        ('email3', 'password2'),
        ('email4', 'password3'),
    ])
    def test_wrong_email_or_password(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form_component.fill(email, password)
        login_page.login_form_component.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()

    @pytest.mark.already_signed_in
    def test_sign_in(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

    def test_successful_authorization(self, login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit_registration_page()
        registration_page.registration_form_component.fill_form(email = "email@email.com", username="username111", password="password11")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_nav_bar_visibility("username111")
        dashboard_page.side_bar_component.check_visible()
        dashboard_page.side_bar_component.click_logout()
        login_page.login_form_component.fill(email = "email@email.com", password="password11")
        login_page.click_login_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_nav_bar_visibility("username111")

    def test_navigate_from_authorisation_to_registration_page(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_register_link()
        registration_page.registration_form_component.check_if_visible()