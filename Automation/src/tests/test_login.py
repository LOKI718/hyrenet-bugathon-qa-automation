import pytest
from src.pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_invalid_login(self):
        self.driver.get("https://app.hyrenet.in/")
        login = LoginPage(self.driver)
        login.login("wrong@email.com", "wrongpassword")
        assert "Dashboard" in self.driver.title
