import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
class Button(BaseElement):
    def type_of(self):
        return "button"

    def check_enabled(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} with name {self.name} is ENABLED and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_be_enabled()

    def check_disabled(self,nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} with name {self.name} is DISABLED and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_be_disabled()

    def check_hidden(self, nth:int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} with name {self.name} is HIDDEN and "data-testid={locator}" at index" {nth}"'):
            expect(locator).to_be_hidden()