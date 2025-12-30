from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")
    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_logged_in(self):
        return self.is_displayed(self.LOGOUT_BUTTON)
    
    def get_page_header(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def logout(self):
        self.click(self.LOGOUT_BUTTON)
    
    def verify_page_loaded(self):
        return "Logged In Successfully" in self.get_page_header() or "successfully logged in" in self.driver.current_url