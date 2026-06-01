from pages.base_page import BasePage
from playwright.sync_api import Page, expect
class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_page_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.students_chart_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_chart_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-line-chart')
        self.courses_chart_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')
        self.scores_chart_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')

    def check_dashboard_title_visibility(self):
        self.check_if_visible(self.dashboard_page_title)
        self.check_text(self.dashboard_page_title,'Dashboard' )
        #expect(self.dashboard_page_title).to_be_visible()
        #expect(self.dashboard_page_title).to_have_text('Dashboard')

    def check_students_chart_visibility(self):
        self.check_if_visible(self.students_chart_title)
        self.check_text(self.students_chart_title,'Students' )
        self.check_if_visible(self.students_chart)

    def check_activities_chart_visibility(self):
        self.check_if_visible(self.activities_chart_title)
        self.check_text(self.activities_chart_title,'Activities' )
        self.check_if_visible(self.activities_chart)

    def check_courses_chart_visibility(self):
        self.check_if_visible(self.courses_chart_title)
        self.check_text(self.courses_chart_title,'Courses' )
        self.check_if_visible(self.courses_chart)

    def check_scores_chart_visibility(self):
        self.check_if_visible(self.scores_chart_title)
        self.check_text(self.scores_chart_title,'Scores' )
        self.check_if_visible(self.scores_chart)

    def visit_dashboard_page(self):
        self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
