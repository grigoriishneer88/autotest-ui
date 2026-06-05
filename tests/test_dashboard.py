from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.dashboard
def test_dashboard_appears_for_signed_in_user(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    #dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state .check_dashboard_title_visibility()

@pytest.mark.dashboard
def test_charts_on_dashboard(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    dashboard_page_with_state.check_dashboard_title_visibility()
    dashboard_page_with_state.check_activities_chart_visibility()
    dashboard_page_with_state.check_courses_chart_visibility()
    dashboard_page_with_state.check_scores_chart_visibility()
    dashboard_page_with_state.check_students_chart_visibility()

@pytest.mark.dashboard
def test_dashboard_page_visibility(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    dashboard_page_with_state.check_dashboard_title_visibility()
    dashboard_page_with_state.check_activities_chart_visibility()
    dashboard_page_with_state.check_courses_chart_visibility()
    dashboard_page_with_state.check_scores_chart_visibility()
    dashboard_page_with_state.navbar_component.check_nav_bar_visibility("test2")
