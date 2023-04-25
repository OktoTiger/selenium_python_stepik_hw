from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from main_page import Main_page
sys.path.append("C:\\Users\\User\\Desktop\\Study_Lessons\\base")
from base_class import Base


class Cart_page(Base):
    

    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser
    """Локатор названия товара и цены товара №1 в корзине"""
    locator_product_1_in_cart = "//a[@id='item_4_title_link']"
    locator_product_price_1_in_cart = "//a[@id='item_4_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №2 в корзине"""
    locator_product_2_in_cart = "//a[@id='item_1_title_link']"
    locator_product_price_2_in_cart = "//a[@id='item_1_title_link']/..//div[2]/div"
    """Локатор названия товара и цены товара №3 в корзине"""
    locator_product_3_in_cart = "//a[@id='item_2_title_link']"
    locator_product_price_3_in_cart = "//a[@id='item_2_title_link']/..//div[2]/div"
    """Локатор названия товара и цены товара №4 в корзине"""
    locator_product_4_in_cart = "//a[@id='item_0_title_link']"
    locator_product_price_4_in_cart = "//a[@id='item_0_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №5 в корзине"""    
    locator_product_5_in_cart = "//a[@id='item_5_title_link']"
    locator_product_price_5_in_cart = "//a[@id='item_5_title_link']/..//div[2]/div[1]"
    """Локатор названия товара и цены товара №6 в корзине"""
    locator_product_6_in_cart = "//a[@id='item_3_title_link']"
    locator_product_price_6_in_cart = "//a[@id='item_3_title_link']/..//div[2]/div[1]"     
    """Локатор нкнопки checkout"""    
    checkout_button = "//button[@id='checkout']"
    
              
    # Getters
    """Методы получения элементов"""      
    def get_product_1_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_1_in_cart)))
         
    def get_product_price_1_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_1_in_cart)))
    
    def get_product_2_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_2_in_cart)))
         
    def get_product_price_2_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_2_in_cart)))         

    def get_product_3_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_3_in_cart)))
         
    def get_product_price_3_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_3_in_cart))) 
    
    def get_product_4_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_4_in_cart)))
         
    def get_product_price_4_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_4_in_cart))) 

    def get_product_5_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_5_in_cart)))
         
    def get_product_price_5_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_5_in_cart)))
    
    def get_product_6_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_6_in_cart)))
         
    def get_product_price_6_in_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_price_6_in_cart)))   
           
    def get_checkout_button(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
      
    
    # Actions
    """Методы нажатия кнопки checkout"""           
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print ("Click checkout_button")  
        

    # Methods
    """Метод проверки названия продукта"""
    def product_confirmation_1(self):
        mp_1 = Main_page(self.browser)
        self.assert_word(self.get_product_1_in_cart(),mp_1.get_product_1_name())

    def product_confirmation_2(self):
        mp_2 = Main_page(self.browser)
        self.assert_word(self.get_product_2_in_cart(),mp_2.get_product_2_name())
        
    def product_confirmation_3(self):
        mp_3 = Main_page(self.browser)
        self.assert_word(self.get_product_3_in_cart(),mp_3.get_product_3_name())
        
    def product_confirmation_4(self):
        mp = Main_page(self.browser)
        self.assert_word(self.get_product_4_in_cart(),mp.get_product_4_name())
        
    def product_confirmation_5(self):
        mp = Main_page(self.browser)
        self.assert_word(self.get_product_5_in_cart(),mp.get_product_5_name())

    def product_confirmation_6(self):
        mp = Main_page(self.browser)
        self.assert_word(self.get_product_6_in_cart(),mp.get_product_6_name())
    
    """Метод проверки стоимости продукта"""
    
    def product_price_confirmation_1(self):
        mp_price1 = Main_page(self.browser)
        self.assert_word(self.get_product_price_1_in_cart(),mp_price1.get_product_1_price())
            
    def product_price_confirmation_2(self):
        mp_price2 = Main_page(self.browser)
        self.assert_word(self.get_product_price_2_in_cart(),mp_price2.get_product_2_price()) 
 
    def product_price_confirmation_3(self):
        mp_price3 = Main_page(self.browser)
        self.assert_word(self.get_product_price_3_in_cart(),mp_price3.get_product_3_price())
        
    def product_price_confirmation_4(self):
        mp_price4 = Main_page(self.browser)
        self.assert_word(self.get_product_price_4_in_cart(),mp_price4.get_product_4_price())        
         
    def product_price_confirmation_5(self):
        mp = Main_page(self.browser)
        self.assert_word(self.get_product_price_5_in_cart(),mp.get_product_5_price()) 
 
    def product_price_confirmation_6(self):
        mp = Main_page(self.browser)
        self.assert_word(self.get_product_price_6_in_cart(),mp.get_product_6_price()) 
