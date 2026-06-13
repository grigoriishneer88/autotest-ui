from re import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def visit(self,url:str):
        self.page.goto(url, wait_until="networkidle")

    def reload(self):
        self.page.reload(wait_until="networkidle")

    def check_if_visible(self, element):
        expect(element).to_be_visible()

    def check_text(self, element, text):
        expect(element).to_have_text(text)

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)