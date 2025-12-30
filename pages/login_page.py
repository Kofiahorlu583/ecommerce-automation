from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    
    PAGE_URL = "https://practicetestautomation.com/practice-test-login/"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate(self):
        self.navigate_to(self.PAGE_URL)
        time.sleep(1)
    
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def is_error_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)