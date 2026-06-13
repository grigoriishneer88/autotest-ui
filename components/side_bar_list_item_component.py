from re import Pattern

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class SideBarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier : str):
        super().__init__(page)
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        #self.title = Text(page, f'{title_id}-list-item-title-text', 'Title')
        self.button = Text(page, f'{identifier}-drawer-list-item-title-text', 'Button')

    def check_visible(self, title:str):
        #self.title.check_visible()
        self.icon.check_visible()
        self.button.check_have_text(title)
        self.button.check_visible()

    def navigate(self, url:Pattern[str]):
        self.button.click()
        self.check_current_url(url)