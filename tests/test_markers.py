import pytest

@pytest.mark.smoke
def test_some_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.critical
def test_critical_login():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_1(self):
        ...
    def test_2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_reset_password(self):
        ...

    def test_logout(self):
        ...

@pytest.mark.ui
class TestUI:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_sign_up_form(self):
        pass