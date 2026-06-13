from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        #self.email_input = page.locator('//*[@id=":r0:"]')
        self.email_input = Input(page, 'login-form-email-input', 'email' )
        #self.password_input = page.locator('//*[@id=":r1:"]')
        self.password_input = Input(page, 'login-form-password-input', 'password' )

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)

    def check_visible(self, email: str, password: str):
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)