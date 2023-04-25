from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from base_class import Base
from cart_page import Cart_page


class Payment_page(Base):
    
    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser
    
    # Locators
    """Локатор названия товара и цены товара №1"""   
    locator_product_1_finish = "//a[@id='item_4_title_link']"
    locator_product_price_1_finish = "//a[@id='item_4_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №2"""   
    locator_product_2_finish = "//a[@id='item_1_title_link']"
    locator_product_price_2_finish = "//a[@id='item_1_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №3"""   
    locator_product_3_finish = "//a[@id='item_2_title_link']"
    locator_product_price_3_finish = "//a[@id='item_2_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №4"""    
    locator_product_4_finish = "//a[@id='item_0_title_link']"
    locator_product_price_4_finish = "//a[@id='item_0_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №5"""       
    locator_product_5_finish = "//a[@id='item_5_title_link']"
    locator_product_price_5_finish = "//a[@id='item_5_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №6"""    
    locator_product_6_finish = "//a[@id='item_3_title_link']"
    locator_product_price_6_finish = "//a[@id='item_3_title_link']/..//div[2]/div[1]" 
    """Локатор кнопки"""   
    locator_finish_button = "//button[@id='finish']"
    
    
           
    # Getters
    """Методы получения элементов"""  
    def get_product_1_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_1_finish)))
         
    def get_product_price_1_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_1_finish)))    
    
    def get_product_2_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_2_finish)))
         
    def get_product_price_2_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_2_finish)))        
    
    def get_product_3_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_3_finish)))
         
    def get_product_price_3_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_3_finish)))    
    
    
    def get_product_4_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_4_finish)))
         
    def get_product_price_4_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_4_finish)))        
    
    def get_product_5_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_5_finish)))
         
    def get_product_price_5_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_5_finish)))        
    
    def get_product_6_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_6_finish)))
         
    def get_product_price_6_finish(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_6_finish)))        
    
        
    def get_finish_button(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_finish_button)))
    
    # Actions
    """Метод нажатия на кнопку"""  
    def click_finish_button(self):
        self.get_finish_button().click()
        print ("Click finish_button")     
        
    
    # Methods
    """Методы проверки названия товара и цены товара""" 
    def product_confirmation_1_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_1_finish(),cp_1.get_product_1_in_cart())
        print("Проверка товара 1 на странице finish")
    
    def product_price_confirmation_1(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_1_finish(),cp_price1.get_product_price_1_in_cart())
        print("Проверка цены товара 1 на странице finish")
            
    def product_confirmation_2_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_2_finish(),cp_1.get_product_2_in_cart())
        print("Проверка товара 2 на странице finish")
    
    def product_price_confirmation_2(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_2_finish(),cp_price1.get_product_price_2_in_cart())
        print("Проверка цены товара 2 на странице finish")
    
    def product_confirmation_3_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_3_finish(),cp_1.get_product_3_in_cart())
        print("Проверка товара 3 на странице finish")
    
    def product_price_confirmation_3(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_3_finish(),cp_price1.get_product_price_3_in_cart())
        print("Проверка цены товара 3 на странице finish")
        
    def product_confirmation_4_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_4_finish(),cp_1.get_product_4_in_cart())
        print("Проверка товара 4 на странице finish")
    
    def product_price_confirmation_4(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_4_finish(),cp_price1.get_product_price_4_in_cart())
        print("Проверка цены товара 4 на странице finish")
        
    def product_confirmation_5_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_5_finish(),cp_1.get_product_5_in_cart())
        print("Проверка товара 5 на странице finish")
    
    def product_price_confirmation_5(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_5_finish(),cp_price1.get_product_price_5_in_cart())
        print("Проверка цены товара 5 на странице finish")          
    
    def product_confirmation_6_finish(self):
        cp_1 = Cart_page(self.browser)
        self.assert_word(self.get_product_6_finish(),cp_1.get_product_6_in_cart())
        print("Проверка товара 6 на странице finish")
    
    def product_price_confirmation_6(self):
        cp_price1 = Cart_page(self.browser)
        self.assert_word(self.get_product_price_6_finish(),cp_price1.get_product_price_6_in_cart())
        print("Проверка цены товара 6 на странице finish")      
    
    def payment(self):
        self.click_finish_button()
        
    



