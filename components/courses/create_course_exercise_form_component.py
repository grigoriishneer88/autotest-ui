import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.delete_exercise_button = Button(page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", 'Delete Exercise')
        self.subtitle = Text(page, 'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text', 'Exercise Subtitle')
        self.title_input = Input(page, 'create-course-exercise-form-title-{exercise_index}-input', 'Title')
        self.description_input = Input(page, 'create-course-exercise-form-description-{exercise_index}-input', 'Description')

    @allure.step('Check create exercise form is visible at index "{index}')
    def create_exercise_form_visibility(self, exercise_index:int):
        self.subtitle.check_visible(index = exercise_index)
        self.title_input.check_visible(index = exercise_index)
        self.description_input.check_visible(index = exercise_index)

    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)

    @allure.step('Fill create exercise form at index "{index}"')
    def fill_create_exercise_form(self, exercise_index:int, exercise_title:str, exercise_description:str):


        self.title_input.fill(exercise_title, index = exercise_index)
        self.title_input.check_have_value(exercise_title, index = exercise_index)
        self.description_input.fill(exercise_description, index = exercise_index)
        self.description_input.check_have_value(exercise_description, index = exercise_index)

        self.subtitle.check_visible(index = exercise_index)
        self.subtitle.check_have_text(f"#{exercise_index+1} Exercise", index = exercise_index)
        self.title_input.check_visible(index = exercise_index)
        self.title_input.check_have_value(exercise_title, index = exercise_index)
        self.description_input.check_visible(index = exercise_index)
        self.description_input.check_have_value(exercise_description, index = exercise_index)


