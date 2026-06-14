from allure_commons.types import Severity
from playwright.sync_api import Page
import pytest
import allure
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.already_signed_in
@allure.tag(AllureTags.REGRESSION.value, AllureTags.AUTHORISATION.value)
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.AUTHENTICATION.value)
@allure.story(AllureStories.AUTHORISATION.value)
class TestAuthorisation:
    @pytest.mark.regression
    @pytest.mark.authorisation
    @pytest.mark.parametrize('email, password', [
        ('email1', 'password'),
        ('email2', 'password1'),
        ('email3', 'password2'),
        ('email4', 'password3'),
    ])
    @allure.tag(AllureTags.USER_LOGIN.value)
    @allure.title("Testing authorisation with wrong email or wrong password")
    @allure.severity(Severity.CRITICAL.value)
    def test_wrong_email_or_password(self, login_page: LoginPage, email: str, password: str):
        # allure.dynamic.title(f"Testing authorisation with wrong email:{email} or wrong password : {password}")
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form_component.fill(email, password)
        login_page.login_form_component.check_visible(email, password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_alert()

    @allure.title("Dashboard available after authorisation with proper email and password")
    @pytest.mark.already_signed_in
    def test_sign_in(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

    @allure.severity(Severity.BLOCKER.value)
    @allure.tag(AllureTags.USER_LOGIN.value)
    @allure.title("Testing authorisation with proper email and password")
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


    @allure.title("Navigation from Login page to Registration page")
    @allure.tag(AllureTags.NAVIGATION.value)
    @allure.severity(Severity.NORMAL.value)
    def test_navigate_from_authorisation_to_registration_page(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_register_link()
        registration_page.registration_form_component.check_if_visible()