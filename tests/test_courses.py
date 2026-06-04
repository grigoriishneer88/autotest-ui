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
    create_course_page.upload_preview_image('/Users/grigorii/PycharmProjects/autotests1/test_data/Image_created_with_a_mobile_phone.png')
    create_course_page.check_upload_image_view_visibility(is_image_uploaded=True)
    create_course_page.click_create_course_button()
    courses_list_page.check_create_course_button_visibility()
    courses_list_page.check_courses_title_visibility()
    courses_list_page.course_view.check_visible(
        0,
        'course1',
        11,
        2,
        12,
    )
