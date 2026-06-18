from playwright.sync_api import Page, expect
import allure

class BaseElement:
    def __init__(self, page:Page, locator:str, name:str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, nth:int = 0, **kwargs):
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data-testid={locator}" at index" {nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self,nth:int = 0,**kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Clicking {self.type_of} with name {self.name} and "data-testid={locator}" at index" {nth}"'):
            locator.click()

    def check_visible(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking {self.type_of} with name {self.name} is VISIBLE and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_be_visible()

    def check_have_text(self, text:str,nth:int = 0,**kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} with name {self.name} has text {text} and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_have_text(text)

    @property
    def type_of(self):
        return "base element"