from playwright.sync_api import sync_playwright
from config import settings
from pages.authentication.registration_page import RegistrationPage

pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages",
    "fixtures.allure"
)

