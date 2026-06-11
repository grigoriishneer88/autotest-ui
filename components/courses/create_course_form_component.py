from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        # create course form
        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = page.get_by_test_id(
            'create-course-form-estimated-time-input').locator('input')
        self.create_course_description_input = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def check_visible(self):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_description_input).to_be_visible()
        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_be_visible()

    def fill(self, title, estimated, description, max_score, min_score):
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)
        self.create_course_estimated_time_input.fill(estimated)
        expect(self.create_course_estimated_time_input).to_have_value(estimated)
        self.create_course_description_input.fill(description)
        expect(self.create_course_description_input).to_have_value(description)
        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input).to_have_value(max_score)
        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input).to_have_value(min_score)