from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseExerciseFormComponent(BaseComponent):

    def create_exercise_form_visibility(self, exercise_index:int):
        subtitle = self.page.get_by_test_id(f'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text')
        title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        description = self.page.get_by_test_id(f'create-course-exercise-form-description-{exercise_index}-input')
        expect(title).to_be_visible()
        expect(description).to_be_visible()
        expect(subtitle).to_be_visible()

    def click_delete_button(self, index: int):
        self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-delete-exercise-button").click()

    def fill_create_exercise_form(self, exercise_index:int, exercise_title:str, exercise_description:str):
        title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        description = self.page.get_by_test_id(f'create-course-exercise-form-description-{exercise_index}-input')

        title.fill(exercise_title)
        expect(title).to_have_text(exercise_title)
        description.fill(exercise_description)
        expect(description).to_have_text(exercise_description)
