import pytest

from fixtures.pages import courses_list_page
from pages.courses_list_page import CoursesPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage


@pytest.mark.courses
def test_add_course(create_course_page:CreateCoursePage, courses_list_page: CoursesPage):
    create_course_page.visit_create_course_page()
    create_course_page.check_create_course_form_visibility()
    create_course_page.check_exercises_title_visibility()
    create_course_page.click_create_new_exercise_button_visibility()
    create_course_page.check_exercises_empty_view_visibility()
    create_course_page.fill_create_course_form(
        'course1',
        '12',
        'course 1 description',
        '11',
        '2'
    )
    create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)

    create_course_page.upload_image_widget.upload_preview_image('/Users/grigorii/PycharmProjects/autotests1/test_data/Image_created_with_a_mobile_phone.png')
    create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
    create_course_page.click_create_course_button()
    courses_list_page.toolbar_view_component.check_create_course_button_visibility()
    courses_list_page.toolbar_view_component.check_courses_title_visibility()
    courses_list_page.course_view.check_visible(
        0,
        'course1',
        11,
        2,
        12,
    )
def test_empty_course_list (courses_list_page: CoursesPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.navbar_component.check_nav_bar_visibility('test2')
    courses_list_page.check_empty_view_visibility()
    courses_list_page.empty_view.check_visible('There is no results','Results from the load test pipeline will be displayed here')
    courses_list_page.toolbar_view_component.check_courses_title_visibility()
    courses_list_page.toolbar_view_component.check_create_course_button_visibility()