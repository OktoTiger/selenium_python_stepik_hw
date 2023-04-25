from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C:\\Users\\User\\Desktop\\Study_Lessons\\base")
from base_class import Base


class Main_page(Base):
    

    def __init__(self,browser):
        super().__init__(browser)
        self.browser = browser
    """Локаторы для первого товара"""
    locator_product_1_name = "//a[@id='item_4_title_link']" # название 1 товара в сторе
    locator_product_1_price = "//button[@id='remove-sauce-labs-backpack']/../div" # цена 1 товара в сторе 
    locator_select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']" #добавление 1 товара в корзину
    """Локаторы для второго товара"""
    locator_product_2_name = "//a[@id='item_1_title_link']"  # название 2 товара в сторе
    locator_product_2_price = "//button[@id='remove-sauce-labs-bolt-t-shirt']/..//div" # цена 2 товара в сторе 
    locator_select_product_2 =  "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']" #добавление 2 товара в корзину
    """Локаторы для третьего товара"""
    locator_product_3_name = "//a[@id='item_2_title_link']" # название 3 товара в сторе
    locator_product_3_price = "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div" # цена 3 товара в сторе 
    locator_select_product_3 = "//button[@id='add-to-cart-sauce-labs-onesie']" #добавление 3 товара в корзину
    """Локаторы для четвертого товара"""
    locator_product_4_name = "//a[@id='item_0_title_link']" # название 4 товара в сторе
    locator_product_4_price = "//button[@id='add-to-cart-sauce-labs-bike-light']/../div" # цена 4 товара в сторе  
    locator_select_product_4 = "//button[@id='add-to-cart-sauce-labs-bike-light']" #добавление 4 товара в корзину
    """Локаторы для пятого товара"""    
    locator_product_5_name = "//a[@id='item_5_title_link']" # название 5 товара в сторе
    locator_product_5_price = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']/../div" # цена 5 товара в сторе 
    locator_select_product_5 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']" #добавление 5 товара в корзину
    """Локаторы для шестого товара"""    
    locator_product_6_name = "//a[@id='item_3_title_link']" # название 6 товара в сторе
    locator_product_6_price = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']/../div" # цена 6 товара в сторе 
    locator_select_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']" #добавление 6 товара в корзину
    """Локаторы для корзины"""    
    locator_cart = "//div[@id='shopping_cart_container']"  
           
    # Getters
    """Продукт номер 1"""
    def get_product_1_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_1_name)))
    def get_product_1_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_1_price)))
    def get_select_product_1(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_1)))
    """Продукт номер 2"""
    def get_product_2_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_2_name)))
    def get_product_2_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_2_price)))
    def get_select_product_2(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_2)))
    """Продукт номер 3"""
    def get_product_3_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_3_name)))
    def get_product_3_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_3_price)))
    def get_select_product_3(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_3)))
    """Продукт номер 4"""
    def get_product_4_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_4_name)))
    def get_product_4_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_4_price)))
    def get_select_product_4(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_4)))
    """Продукт номер 5"""
    def get_product_5_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_5_name)))
    def get_product_5_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_5_price)))
    def get_select_product_5(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_5)))
    """Продукт номер 6"""
    def get_product_6_name(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_6_name)))
    def get_product_6_price(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_6_price)))
    def get_select_product_6(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_select_product_6)))
    """Продукт корзина"""    
    def get_cart(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_cart)))   
    
    # Actions
    """Выбираем товар"""
       
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print ("Click product 1")
    
    def click_select_product_2(self):
        self.get_select_product_2().click()
        print ("Click product 2")
        
    def click_select_product_3(self):
        self.get_select_product_3().click()
        print ("Click product 3")
    
    def click_select_product_4(self):
        self.get_select_product_4().click()
        print ("Click product 4")
    
    def click_select_product_5(self):
        self.get_select_product_5().click()
        print ("Click product 5")
    
    def click_select_product_6(self):
        self.get_select_product_6().click()
        print ("Click product 6")
        
    """Нажимам на иконку корзины"""        
    def click_cart(self):
        self.get_cart().click()
        print ("Click cart")   
           
    # Methods
    def select_product_1(self):
        # locator = WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_product_3_price)))
        # print("Цена Товара номер 3 " + locator.text)
        self.click_select_product_1()
        self.click_cart()
        
    def select_product_2(self):
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.click_select_product_3()
        self.click_cart()
        
    def select_product_4(self):
        self.click_select_product_4()
        self.click_cart()
        
    def select_product_5(self):
        self.click_select_product_5()
        self.click_cart()
        
    def select_product_6(self):
        self.click_select_product_6()
        self.click_cart()