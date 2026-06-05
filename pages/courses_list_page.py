from components.courses.cource_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page,'courses-list')
        self.toolbar_view_component = CoursesListToolbarViewComponent(page)
        self.navbar_component = NavbarComponent(page)
        # self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        # self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        # self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        # self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        # self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        # self.course_title = page.get_by_test_id('course-widget-title-text')
        # self.course_image = page.get_by_test_id('course-preview-image')
        # self.course_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        # self.course_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        # self.course_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        # self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item-icon')
        # self.course_delete_button = page.get_by_test_id('course-view-edit-menu-item-icon')

    # def check_courses_title_visibility(self):
    #
    #     self.check_if_visible(self.courses_title)
    #     self.check_text(self.courses_title,'Courses')
    #
    # def check_create_course_button_visibility(self):
    #     self.check_if_visible(self.create_course_button)

    def check_empty_view_visibility(self):
        self.empty_view.check_visible(title = "There is no results",
                                      description="Results from the load test pipeline will be displayed here"
                                      )
        # self.check_if_visible(self.empty_view_icon)
        # self.check_if_visible(self.empty_view_title)
        # self.check_text(self.empty_view_title, 'There is no results')
        # self.check_if_visible(self.empty_view_description)
        # self.check_text(self.empty_view_description, 'Results from the load test pipeline will be displayed here')
    #
    # def click_create_course_button(self, title):
    #     self.create_course_button.click()

    # def check_course_card_visibility_by_index(self, index, title, max_score, min_score, estimated_time):
    #     expect(self.course_image.nth(index)).to_be_visible()
    #     expect(self.course_title.nth(index)).to_be_visible()
    #     expect(self.course_title.nth(index)).to_have_text(title)
    #     expect(self.course_max_score.nth(index)).to_be_visible()
    #     expect(self.course_min_score.nth(index)).to_have_text(f"Max score: {max_score}")
    #     expect(self.course_min_score.nth(index)).to_be_visible(f"Min score: {min_score}")
    #     expect(self.course_estimated_time.nth(index)).to_be_visible()
    #     expect(self.course_estimated_time.nth(index)).to_have_text(f"Estimated time: {estimated_time}")


    # def find_course_index_by_title(self, title):
    #     course_names = self.course_title.all()
    #     course_index = None
    #     for index, course_name in course_names:
    #         course_name_text = course_name.text_content()
    #         if title == course_name_text:
    #             course_index = index
    #     return course_index

    # def check_course_card_visibility_by_course_name(self, title, max_score, min_score, estimated_time):
    #     #course_names = self.course_title.all()
    #     course_index = self.find_course_index_by_title(title)
    #     # for index, course_name in course_names:
    #     #     course_name_text = course_name.text_content()
    #     #     if title == course_name_text:
    #     #         course_index = index
    #     expect(self.course_image.nth(course_index)).to_be_visible()
    #     expect(self.course_title.nth(course_index)).to_be_visible()
    #     expect(self.course_title.nth(course_index)).to_have_text(title)
    #     expect(self.course_max_score.nth(course_index)).to_be_visible()
    #     expect(self.course_min_score.nth(course_index)).to_have_text(f"Max score: {max_score}")
    #     expect(self.course_min_score.nth(course_index)).to_be_visible(f"Min score: {min_score}")
    #     expect(self.course_estimated_time.nth(course_index)).to_be_visible()
    #     expect(self.course_estimated_time.nth(course_index)).to_have_text(f"Estimated time: {estimated_time}")

    # def click_edit_course_button_by_title(self, title:str):
    #     course_index = self.find_course_index_by_title(title)
    #     self.course_menu_button.nth(course_index).click()
    #     expect(self.course_edit_button.nth(course_index)).to_be_visible()
    #     self.course_edit_button.nth(course_index).click()

    # def click_delete_course_button_by_title(self, title:str):
    #     course_index = self.find_course_index_by_title(title)
    #     self.course_menu_button.nth(course_index).click()
    #     expect(self.course_edit_button.nth(course_index)).to_be_visible()
    #     self.course_delete_button.nth(course_index).click()
    #
    # def click_edit_course_button_by_index(self, index:int):
    #     self.course_menu_button.nth(index).click()
    #     expect(self.course_edit_button.nth(index)).to_be_visible()
    #     self.course_edit_button.nth(index).click()
    #
    # def click_delete_course_button_by_index(self, index):
    #     self.course_menu_button.nth(index).click()
    #     expect(self.course_edit_button.nth(index)).to_be_visible()
    #     self.course_delete_button.nth(index).click()