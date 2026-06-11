from playwright.sync_api import Page,expect
from components.base_component import BaseComponent


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_new_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')

    def check_visible(self):
        expect(self.create_new_exercise_button).to_be_visible()
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def click_create_new_exercise_button(self):
        self.create_new_exercise_button.click()
