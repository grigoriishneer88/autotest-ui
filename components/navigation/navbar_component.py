from playwright.sync_api import Page, expect

from elements.text import Text


class NavbarComponent:
    def __init__(self, page: Page):
        self.page = page
        self.app_title = Text(page,'navigation-navbar-app-title-text', 'navigation-navbar-app-title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text' , 'navigation-navbar-welcome-title')

    def check_nav_bar_visibility(self, username):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')
        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')