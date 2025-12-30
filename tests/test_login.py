import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time


class TestLogin:
    
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """Test valid login"""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("student", "Password123")
        
        time.sleep(2)
        home_page = HomePage(driver)
        
        assert home_page.is_logged_in(), "Logout button not found - login failed"
        assert home_page.verify_page_loaded(), "Success message not found"
        print("✓ Valid login test passed!")
    
    @pytest.mark.regression
    def test_invalid_password(self, driver):
        """Test invalid password"""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("student", "WrongPassword")
        
        time.sleep(2)
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "invalid" in error_text.lower(), f"Unexpected error: {error_text}"
        print("✓ Invalid password test passed!")
    
    @pytest.mark.regression
    def test_invalid_username(self, driver):
        """Test invalid username"""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("invaliduser", "Password123")
        
        time.sleep(2)
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "invalid" in error_text.lower(), f"Unexpected error: {error_text}"
        print("✓ Invalid username test passed!")
    
    @pytest.mark.smoke
    def test_logout(self, driver):
        """Test logout functionality"""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("student", "Password123")
        
        time.sleep(2)
        home_page = HomePage(driver)
        assert home_page.is_logged_in(), "Login failed"
        
        home_page.logout()
        time.sleep(2)
        
        assert "login" in driver.current_url.lower(), "Not redirected to login page"
        print("✓ Logout test passed!")