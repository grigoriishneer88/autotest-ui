from base_element import BaseElement
class Input(BaseElement):
    def set_input_files(self, file:str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)