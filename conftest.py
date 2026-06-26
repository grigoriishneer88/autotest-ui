
from playwright.sync_api import sync_playwright
from config import settings

pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages",
    "fixtures.allure"
)


def pytest_configure(config):
    """Хук выполняется строго в одном главном процессе перед стартом воркеров xdist."""
    # Проверяем, что это главный процесс, а не дочерний воркер gw0/gw1
    if not hasattr(config, "workerinput"):
        # Создаем папку для стейта, если её ещё нет
        settings.browser_state_file.parent.mkdir(parents=True, exist_ok=True)

        # Запускаем изолированный Playwright для генерации сессии
        with sync_playwright() as p:
            brw = p.chromium.launch(headless=settings.headless)
            context = brw.new_context(base_url=settings.get_base_url())
            page = context.new_page()

            # Твоя стандартная логика авторизации/регистрации
            page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
            page.locator('input[type="email"]').fill(settings.test_user.email)
            page.locator('input[type="password"]').fill(settings.test_user.password)
            page.locator('input[placeholder="Name"]').fill(settings.test_user.username)
            page.locator('button', has_text='Зарегистрироваться').click()
            page.wait_for_load_state('networkidle')

            # Сохраняем чистый JSON-файл
            context.storage_state(path=str(settings.browser_state_file))
            context.close()
            brw.close()