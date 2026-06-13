import pytest

from pages.dashboard.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.dashboard
class TestDashboard:
    def test_dashboard_appears_for_signed_in_user(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        # dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

    def test_charts_on_dashboard(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
        dashboard_page_with_state.activities_chart_view.visible("Activities")
        dashboard_page_with_state.courses_chart_view.visible("Courses")
        dashboard_page_with_state.scores_chart_view.visible("Scores")
        dashboard_page_with_state.students_chart_view.visible("Students")

    def test_dashboard_page_visibility(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
        dashboard_page_with_state.activities_chart_view.visible("Activities")
        dashboard_page_with_state.courses_chart_view.visible("Courses")
        dashboard_page_with_state.scores_chart_view.visible("Scores")
        dashboard_page_with_state.students_chart_view.visible("Students")
        dashboard_page_with_state.navbar_component.check_nav_bar_visibility("test2")
