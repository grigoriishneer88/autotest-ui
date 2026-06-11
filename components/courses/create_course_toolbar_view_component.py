from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def click_create_course_button(self):
        self.button.click()

    def check_visible(self, is_create_course_disabled=True):
        if is_create_course_disabled:
            expect(self.button).to_be_disabled()
        else:
            expect(self.button).to_be_visible()

