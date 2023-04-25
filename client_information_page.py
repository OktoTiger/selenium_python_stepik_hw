from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from base_class import Base


class Client_information_page(Base):
    
    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser
    
    # Locators
    """Локаторы для клиентской формы"""
    locator_first_name = "//input[@id='first-name']"
    locator_last_name = "//input[@id='last-name']"
    locator_postal_code = "//input[@id='postal-code']"
    locator_button_continue = "//input[@id='continue']"       
    
    # Getters
    """Методы получения элементов"""
    def get_first_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_first_name)))
    
    def get_last_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_last_name)))
    
    def get_postal_code(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_postal_code)))
    
    def get_button_continue(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_button_continue)))       
    
    # Actions
    """Методы заполнения формы"""
    def input_first_name (self, first_name):
        self.get_first_name().send_keys(first_name)
        print ("Input first_name")
        
    def input_last_name (self, last_name):
        self.get_last_name().send_keys(last_name)
        print ("Input last_name")
    
    def input_postal_code (self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print ("Input postal_code")
       
    def click_button_continue (self):
        self.get_button_continue().click()
        print ("Input button_continue")  
    
    # Methods
    def input_information(self):
        self.input_first_name("Дмитрий")
        self.input_last_name("Назаров")
        self.input_postal_code("449200")
        self.click_button_continue()


