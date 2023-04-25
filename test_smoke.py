from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import sys
from payment_page import Payment_page
sys.path.append("C:\\Users\\User\\Desktop\\Study_Lessons\\project_dz")
from cart_page import Cart_page
from client_information_page import Client_information_page
from login_page import Login_page
from main_page import Main_page



def test_buy_product():
    print("Приветствую тебя в нашем интернет магазине")
    print("Выберете один из следующих товаров и укажите его номер\n1-Sauce Labs Backpack\n2-Sauce Labs Bolt T-Shirt\n3-Sauce Labs Onesie\n4-Sauce Labs Bike Light\n5-Sauce Labs Fleece Jacket\n6-Test.allTheThings() T-Shirt (Red)")
    item_number = input()
    print(item_number) 
        
    # pytest -s -v test_smoke.py    
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(chrome_options=options)
        
        
    if item_number == "1":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_1()
        
        cp= Cart_page(browser)
        cp.product_confirmation_1()
        cp.product_price_confirmation_1()
        cp.click_checkout_button()
        
        cip = Client_information_page(browser)
        cip.input_information()
        
        pp= Payment_page(browser)
        pp.product_confirmation_1_finish()
        pp.product_price_confirmation_1()
        pp.payment()
        
        time.sleep(4)
        
    elif item_number == "2":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_2()
        
        cp = Cart_page(browser)
        cp.product_confirmation_2()
        cp.product_price_confirmation_2() # перепроверить локатор
        cp.click_checkout_button()
        
        cip = Client_information_page(browser)
        cip.input_information()
        
        pp = Payment_page(browser)
        pp.product_confirmation_2_finish()
        pp.product_price_confirmation_2()
        pp.payment()
        
        time.sleep(4)
        
    elif item_number == "3":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_3()
        
        cp = Cart_page(browser)
        cp.product_confirmation_3()
        cp.product_price_confirmation_3()
        cp.click_checkout_button()
        
        cip = Client_information_page(browser)
        cip.input_information()        
        
        pp = Payment_page(browser)
        pp.product_confirmation_3_finish()
        pp.product_price_confirmation_3()
        pp.payment()
        
        time.sleep(5)
        
    elif item_number == "4":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_4()
        
        cp = Cart_page(browser)
        cp.product_confirmation_4()
        cp.product_price_confirmation_4()
        cp.click_checkout_button()

        cip = Client_information_page(browser)
        cip.input_information()
                
        pp = Payment_page(browser)
        pp.product_confirmation_4_finish()
        pp.product_price_confirmation_4()
        pp.payment()
        
        time.sleep(5)
        
    elif item_number == "5":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_5()
        
        cp = Cart_page(browser)
        cp.product_confirmation_5()
        cp.product_price_confirmation_5()
        cp.click_checkout_button()

        cip = Client_information_page(browser)
        cip.input_information()
                
        pp = Payment_page(browser)
        pp.product_confirmation_5_finish()
        pp.product_price_confirmation_5()
        pp.payment()
        time.sleep(5)
        
    elif item_number == "6":
        login = Login_page(browser)
        login.authorization()
        
        mp = Main_page(browser)
        mp.select_product_6()
        
        cp = Cart_page(browser)
        cp.product_confirmation_6()
        cp.product_price_confirmation_6()
        cp.click_checkout_button()

        cip = Client_information_page(browser)
        cip.input_information()
               
        pp = Payment_page(browser)
        pp.product_confirmation_5_finish()
        pp.product_price_confirmation_5()
        pp.payment()        
        
        time.sleep(5)
        
    else: 
        print("Необходимо выьрать товар.Нажмите цифру от 1 до 6")

       
time.sleep(5)



