from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
sys.path.append("C:\\Users\\User\\Desktop\\Study_Lessons\\base")
from base_class import Base

"""
Методы для login page

"""

class Login_page(Base):
    
    link = "https://www.saucedemo.com/"
    
    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser
    
    # Locators
    locator_user_name = "//input[@id='user-name']"
    locator_password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"
           
    # Getters
    
    def get_user_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_user_name)))
    
    def get_password(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_password)))
    
    def get_button_login(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    
       
    # Actions
    
    def input_user_name (self, user_name):
        self.get_user_name().send_keys(user_name)
        print ("Input user name")
        
    def input_password (self, password):
        self.get_password().send_keys(password)
        print ("Input password")
        
    def click_login_button (self):
        self.get_button_login().click()
        print ("Click button")  
    
    # Methods
    def authorization(self):
        self.browser.get(self.link)
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()

