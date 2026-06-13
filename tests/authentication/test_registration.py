import pytest
from playwright.sync_api import Page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @pytest.mark.parametrize(
        "email, password, username",  # 1. Имена переменных одной строкой через запятую
        [
            ("test2@test.com", "test2", "test2")
        ]
    )
    @pytest.mark.regression
    @pytest.mark.registration
    @pytest.mark.already_signed_in
    def test_successful_registration(self, chromium_page: Page, dashboard_page: DashboardPage, registration_page: RegistrationPage, email:str, username:str, password:str):
            registration_page.visit_registration_page()
            registration_page.registration_form_component.fill_form(email, username, password)
            registration_page.click_registration_button()
            dashboard_page.dashboard_toolbar_view_component.check_visible()
            dashboard_page.side_bar_component.check_visible()
            dashboard_page.side_bar_component.click_logout()
