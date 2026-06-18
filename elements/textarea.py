import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class TextAria(BaseElement):
    def type_of(self):
        return "textaria"

    def get_locator(self,nth:int = 0,  **kwargs):
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value:str,nth:int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Fill {self.type_of} with name {self.name} by {value} and "data-testid={locator}" at index" {nth}"'):
            locator.fill(value)

    def check_have_value(self, value:str,nth:int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Check that {self.type_of} with name {self.name} has value: {value}, and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_have_value(value)

