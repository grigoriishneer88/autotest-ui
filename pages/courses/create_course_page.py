from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.preview_empty_view = EmptyViewComponent(page,'create-course-preview')
        self.upload_image_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_form = CreateCourseExerciseFormComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)
        #header
        # self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        #exercises area
        #empty exercises aria
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        # self.create_new_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        # self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')

    def visit_create_course_page(self):
        self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # def check_course_title_visibility(self):
    #     self.exercises_title.is_visible()
    #     expect(self.exercises_title).to_be_visible()
    #     expect(self.exercises_title).to_have_text('Create course')

    # def click_create_course_button(self):
    #     self.create_course_button.click()
    #
    # def check_create_course_button_visibility(self):
    #     expect(self.create_course_button).to_be_visible()
    #
    # def check_create_course_button_disabled(self):
    #     expect(self.create_course_button).to_be_disabled()

    def check_preview_empty_view_visibility(self):
        self.preview_empty_view.check_visible(title='No image selected', description='Preview of selected image will be displayed here')

    # def check_exercises_title_visibility(self):
    #     expect(self.exercises_title).to_be_visible()
    #
    # def create_exercises_button_visibility(self):
    #     expect(self.create_new_exercise_button).to_be_visible()
    #
    # def click_create_new_exercise_button(self):
    #     self.create_new_exercise_button.click()
    #
    # def click_create_new_exercise_button_visibility(self):
    #     expect(self.create_new_exercise_button).to_be_visible()

    def check_exercises_empty_view_visibility(self):
        self.exercises_empty_view.check_visible(title='There is no exercises', description='Click on "Create exercise" button to create new exercise')

    def get_exercise_index_by_name(self, title: str):
        exercise_names = self.exercises_title.all()
        exercise_index = None
        for index, exercise_name in exercise_names:
            exercise_name_text = exercise_name.text_content()
            if title == exercise_name_text:
                exercise_index = index
        return exercise_index
