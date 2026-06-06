from playwright.sync_api import Page
from playwright.sync_api import expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, ):    #'create-course-preview - identifier
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page,'create-course-preview')
        # upload image section
        self.image_upload_info_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        self.image_upload_info_title = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        self.image_upload_info_description = page.get_by_test_id(f'{identifier}-image-upload-widget-info-description-text')
        self.upload_button = page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        self.upload_input_file = page.get_by_test_id(f'{identifier}-image-upload-widget-input')

        # full view
        # image section
        self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

        # upload image section
        self.delete_image = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')

    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_info_icon).to_be_visible()
        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')
        expect(self.upload_button).to_be_visible()
        if is_image_uploaded:
            expect(self.delete_image).to_be_visible()
        else:
            expect(self.delete_image).to_be_hidden()

    def click_delete_image_button(self):
        self.delete_image.click()

    def upload_preview_image(self, file: str):
        self.upload_input_file.set_input_files(file)

