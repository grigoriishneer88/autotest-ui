import re

import allure

from components import base_component
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.side_bar_list_item_component import SideBarListItemComponent


class SideBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logout_list_item = SideBarListItemComponent(page,'logout')
        self.courses_list_item = SideBarListItemComponent(page,'courses')
        self.dashboard_list_item = SideBarListItemComponent(page, 'dashboard')

    @allure.step('Check side bar is visible')
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step('Click logout on side bar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on side bar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on side bar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))