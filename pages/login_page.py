from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator('//*[@id=":r0:"]')
        self.password_input = page.locator('//*[@id=":r1:"]')
        self.login_button = page.locator('//*[@id="login-page-login-button"]')
        self.register_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]')

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_register_link(self):
        self.register_link.click()

    def check_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")