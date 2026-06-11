from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.mark.dashboard
def test_dashboard_appears_for_signed_in_user(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    #dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

@pytest.mark.dashboard
def test_charts_on_dashboard(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
    dashboard_page_with_state.activities_chart_view.visible("Activities")
    dashboard_page_with_state.courses_chart_view.visible("Courses")
    dashboard_page_with_state.scores_chart_view.visible("Scores")
    dashboard_page_with_state.students_chart_view.visible("Students")

@pytest.mark.dashboard
def test_dashboard_page_visibility(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit_dashboard_page()
    dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
    dashboard_page_with_state.activities_chart_view.visible("Activities")
    dashboard_page_with_state.courses_chart_view.visible("Courses")
    dashboard_page_with_state.scores_chart_view.visible("Scores")
    dashboard_page_with_state.students_chart_view.visible("Students")
    dashboard_page_with_state.navbar_component.check_nav_bar_visibility("test2")
