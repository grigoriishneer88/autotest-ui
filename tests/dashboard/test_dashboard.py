import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature


@pytest.mark.regression
@pytest.mark.dashboard
@allure.epic(AllureEpic.LMS.value)
@allure.feature(AllureFeature.DASHBOARD.value)
@allure.story(AllureStories.DASHBOARD.value)
class TestDashboard:
    @allure.severity(Severity.NORMAL)
    @allure.title("Dashboard can be viewed for Signed in User")
    @allure.tag(AllureTags.DASHBOARD.value, AllureTags.REGRESSION.value)
    def test_dashboard_appears_for_signed_in_user(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        # dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()

    @allure.severity(Severity.NORMAL)
    @allure.title("Check charts on Dashboard page")
    @allure.tag(AllureTags.DASHBOARD.value, AllureTags.REGRESSION.value)
    def test_charts_on_dashboard(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
        dashboard_page_with_state.activities_chart_view.visible("Activities")
        dashboard_page_with_state.courses_chart_view.visible("Courses")
        dashboard_page_with_state.scores_chart_view.visible("Scores")
        dashboard_page_with_state.students_chart_view.visible("Students")

    @allure.severity(Severity.NORMAL)
    @allure.title("Check Dashboard page items visibility")
    @allure.tag(AllureTags.DASHBOARD.value, AllureTags.REGRESSION.value)
    def test_dashboard_page_visibility(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit_dashboard_page()
        dashboard_page_with_state.dashboard_toolbar_view_component.check_visible()
        dashboard_page_with_state.activities_chart_view.visible("Activities")
        dashboard_page_with_state.courses_chart_view.visible("Courses")
        dashboard_page_with_state.scores_chart_view.visible("Scores")
        dashboard_page_with_state.students_chart_view.visible("Students")
        dashboard_page_with_state.navbar_component.check_nav_bar_visibility("test2")
