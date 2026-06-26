from playwright.sync_api import sync_playwright
from config import settings
from pages.authentication.registration_page import RegistrationPage  # Импортируем твой класс страницы

pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages",
    "fixtures.allure"
)


def pytest_configure(config):
    """Хук выполняется строго в одном главном процессе перед стартом воркеров xdist."""
    if not hasattr(config, "workerinput"):
        settings.browser_state_file.parent.mkdir(parents=True, exist_ok=True)

        with sync_playwright() as p:
            brw = p.chromium.launch(headless=settings.headless)
            context = brw.new_context(base_url=settings.get_base_url())
            page = context.new_page()

            # Используем твою родную логику страниц, как в тестах
            registration_page = RegistrationPage(page=page)
            registration_page.visit(
                "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

            # Заполнение формы через твой компонент
            registration_page.registration_form_component.fill_form(
                email=settings.test_user.email,
                password=settings.test_user.password,
                name=settings.test_user.username
            )
            registration_page.click_registration_button()

            # Даем страницам и кукам стабильно записаться
            page.wait_for_load_state('networkidle')

            context.storage_state(path=str(settings.browser_state_file))
            context.close()
            brw.close()