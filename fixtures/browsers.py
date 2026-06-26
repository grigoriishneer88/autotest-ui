import allure
import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from config import settings
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browser)
def page(request: SubRequest, playwright:Playwright):
    yield from initialize_playwright_page(playwright, test_name = request.node.name, storage_stage = None, browser_type=request.param)


@pytest.fixture(scope="session", autouse=True)  # Добавили autouse=True, чтобы состояние генерировалось автоматически
def initialize_browser_state(playwright: Playwright, tmp_path_factory):
    # Создаем уникальный маркер блокировки процесса во временной папке сессии pytest
    shared_dir = tmp_path_factory.getbasetemp().parent / "shared_state_lock"

    try:
        # os.makedirs атомарен — только один параллельный процесс успеет создать эту папку первым
        os.makedirs(shared_dir)

        # Этот блок выполнит только один главный воркер
        settings.browser_state_file.parent.mkdir(parents=True, exist_ok=True)

        brw = playwright.chromium.launch(headless=settings.headless)
        context = brw.new_context(base_url=settings.get_base_url())
        page = context.new_page()
        registration_page = RegistrationPage(page=page)
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form_component.fill_form(
            email=settings.test_user.email,
            password=settings.test_user.password,
            name=settings.test_user.username
        )
        registration_page.click_registration_button()
        page.wait_for_timeout(1500)  # Даем кукам/токену успеть записаться в контекст

        context.storage_state(path=str(settings.browser_state_file))
        context.close()
        brw.close()

    except FileExistsError:
        # Все остальные процессы ловят эту ошибку и послушно ждут, пока файл допишется
        while not os.path.exists(settings.browser_state_file) or os.path.getsize(settings.browser_state_file) == 0:
            time.sleep(0.5)

@pytest.fixture(params=settings.browser)
def page_with_state(request: SubRequest, playwright:Playwright):
    yield from initialize_playwright_page(playwright, test_name = request.node.name, storage_stage = settings.browser_state_file, browser_type=request.param)

