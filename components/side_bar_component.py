import re

from components import base_component
from playwright.sync_api import Page

from components.side_bar_list_item_component import SideBarListItemComponent


class SideBarComponent(base_component):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logout_list_item = SideBarListItemComponent(page,'logout')
        self.courses_list_item = SideBarListItemComponent(page,'courses')
        self.dashboard_list_item = SideBarListItemComponent(page, 'dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('logout')
        self.courses_list_item.check_visible('courses')
        self.dashboard_list_item.check_visible('dashboard')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        self.logout_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.logout_list_item.navigate(re.compile(r".*/#/dashboard"))