import pytest


@pytest.fixture(autouse = True)
def send_analytics_data():
    print("send_analytics_data - autouse = True\n")
    return "analytics_data"

@pytest.fixture(scope="session")
def settings():
    print("settings - session\n")
    ...
@pytest.fixture(scope="class")
def user():
    print("user - class\n")
    ...
@pytest.fixture(scope="function")
def browser():
    print("browser - function\n")
    ...

class TestUserFlow:
    def test_user_login(self, settings,user,browser):
        ...

    def test_user_create_course(self, settings,user,browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings,user,browser):
        ...