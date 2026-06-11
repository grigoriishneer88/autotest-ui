from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.email_field = page.get_by_test_id("registration-form-email-input").locator('input')
        self.name_field = page.get_by_test_id("registration-form-username-input").locator('input')
        self.password_field = page.get_by_test_id("registration-form-password-input").locator('input')

    def fill_form(self, email:str, username:str, password:str):
        self.email_field.fill(email)
        self.name_field.fill(username)
        self.password_field.fill(password)