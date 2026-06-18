import allure

from elements.base_element import BaseElement
class Input(BaseElement):
    def type_of(self):
        return 'fileinput'
    def set_input_files(self, file:str, nth:int = 0, **kwargs):
        with allure.step(f'Set input file "{file}" to "{self.type_of} with name "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)