from playwright.sync_api import Page, expect

from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page,'create-course-preview')

        #header
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        #empty view

        #image section
        # self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        # self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        # self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        #upload image section
        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.preview_image_upload_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.preview_image_upload_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.input_file = page.get_by_test_id('create-course-preview-image-upload-widget-input')

        #full view
        #image section
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        #upload image section
        self.delete_image = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        #create course form
        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.create_course_description_input = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        #exercises area
        #empty exercises aria
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_new_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        # self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        # self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        # self.exercises_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')


    def check_course_title_visibility(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_create_course_button_visibility(self):
        expect(self.create_course_button).to_be_visible()

    def check_create_course_button_disabled(self):
        expect(self.create_course_button).to_be_disabled()

    def check_preview_empty_view_visibility(self):
        self.preview_empty_view.check_visible(title='No image selected', description='Preview of selected image will be displayed here')
        # expect(self.preview_empty_view_icon).to_be_visible()
        # expect(self.preview_empty_view_title).to_be_visible()
        # expect(self.preview_empty_view_title).to_have_text('No image selected')
        # expect(self.preview_empty_view_description).to_be_visible()
        # expect(self.preview_empty_view_description).to_have_text('Preview of selected image will be displayed here')

    def check_upload_image_view_visibility(self, is_image_uploaded: bool = False ):
        expect(self.preview_image_upload_icon).to_be_visible()
        expect(self.preview_image_upload_title).to_be_visible()
        expect(self.preview_image_upload_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.preview_image_upload_description).to_be_visible()
        expect(self.preview_image_upload_description).to_have_text('Recommended file size 540X300')
        expect(self.preview_image_upload_button).to_be_visible()
        if is_image_uploaded:
            expect(self.delete_image).to_be_visible()
        else:
            expect(self.delete_image).to_be_disabled()

    def click_delete_image_button(self):
        self.delete_image.click()

    def check_preview_image_is_visible(self):
        expect(self.preview_image).to_be_visible()

    def upload_preview_image(self, file:str):
        self.input_file.set_input_files(file)

    def check_create_course_form_visibility(self):
        expect(self.create_course_title_input).to_be_visible()
        #expect(self.create_course_title_input).to_have_value(title)
        expect(self.create_course_estimated_time_input).to_be_visible()
        #expect(self.create_course_estimated_time_input).to_have_value(estimated)
        expect(self.create_course_description_input).to_be_visible()
        #expect(self.create_course_description_input).to_have_value(description)
        expect(self.create_course_max_score_input).to_be_visible()
        #expect(self.create_course_max_score_input).to_have_value(max_score)
        expect(self.create_course_min_score_input).to_be_visible()
        #expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill_create_course_form(self, title, estimated, description, max_score, min_score):
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

    def check_exercises_title_visibility(self):
        expect(self.exercises_title).to_be_visible()

    def create_exercises_button_visibility(self):
        expect(self.create_new_exercise_button).to_be_visible()

    def click_create_new_exercise_button(self):
        self.create_new_exercise_button.click()

    def click_create_new_exercise_button_visibility(self):
        expect(self.create_new_exercise_button).to_be_visible()

    def check_exercises_empty_view_visibility(self):
        self.exercises_empty_view.check_visible(title='There is no exercises', description='Click on "Create exercise" button to create new exercise')
        # expect(self.exercises_empty_view_icon).to_be_visible()
        # expect(self.exercises_empty_view_title).to_be_visible()
        # expect(self.exercises_empty_view_title).to_have_text('There is no exercises')
        # expect(self.exercises_empty_view_description).to_be_visible()
        # expect(self.exercises_empty_view_description).to_have_text('Click on "Create exercise" button to create new exercise')

    def click_delete_exercise_button_by_index(self, index: int):
        self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-delete-exercise-button").click()

    def click_delete_exercise_button_by_exercise_name(self, exercise_title: str):
        exercise_index = self.get_exercise_index_by_id(exercise_title)
        self.page.get_by_test_id(f"create-course-exercise-{exercise_index}-box-toolbar-delete-exercise-button").click()

    def get_exercise_index_by_id(self, title: str):
        exercise_names = self.exercises_title.all()
        exercise_index = None
        for index, exercise_name in exercise_names:
            exercise_name_text = exercise_name.text_content()
            if title == exercise_name_text:
                exercise_index = index
        return exercise_index

    def create_exercise_form_visibility_by_index(self, exercise_index:int):
        exercise_subtitle = self.page.get_by_test_id(f'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text')
        new_exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        new_exercise_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{exercise_index}-input')
        expect(new_exercise_title).to_be_visible()
        expect(new_exercise_description).to_be_visible()
        expect(exercise_subtitle).to_be_visible()


    def create_exercise_form_visibility_by_title(self, title: str):
        exercise_index = self.get_exercise_index_by_id(title)
        exercise_subtitle = self.page.get_by_test_id(f'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text')
        new_exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        new_exercise_description = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{exercise_index}-input')
        expect(new_exercise_title).to_be_visible()
        expect(new_exercise_description).to_be_visible()
        expect(exercise_subtitle).to_be_visible()

    def fill_create_exercise_form_by_index(self, exercise_index:int, exercise_title:str, exercise_description:str):
        new_exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        new_exercise_description = self.page.get_by_test_id(f'create-course-exercise-form-description-{exercise_index}-input')

        new_exercise_title.fill(exercise_title)
        expect(new_exercise_title).to_have_text(exercise_title)
        new_exercise_description.fill(exercise_description)
        expect(new_exercise_description).to_have_text(exercise_description)


    def fill_create_exercise_form_by_title(self, title: str):
        exercise_index = self.get_exercise_index_by_id(title)
        exercise_subtitle = self.page.get_by_test_id(f'create-course-exercise-{exercise_index}-box-toolbar-subtitle-text')
        new_exercise_title = self.page.get_by_test_id(f'create-course-exercise-form-title-{exercise_index}-input')
        new_exercise_description = self.page.get_by_test_id(
            f'create-course-exercise-form-description-{exercise_index}-input')
        expect(new_exercise_title).to_be_visible()
        expect(new_exercise_description).to_be_visible()
        expect(exercise_subtitle).to_be_visible()

    def visit_create_course_page(self):
        self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")