from selenium import webdriver
import pandas as pd
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class scraping_test_me():
    """ """
    def __init__(self, path , website ,pw) -> None:
        
        self.path = path
        self.website = website
        self.pw = pw
        self.driver = ''

    def login_to_website (self):
        
        def set_driver (self):
            
            self.driver = webdriver.Chrome(self.path) 
            self.driver.get(self.website)

        def fill_password (self): 
         
            search= self.driver.find_element_by_id("inputID")
            search.clear()
            search.send_keys(self.pw)
       
        def login(self):

            set_driver(self)
            time.sleep(1)
            fill_password(self)
            login= self.driver.find_element_by_id("btnID")
            login.click()
            time.sleep(2)

        login(self)
    
    def get_text_from_website (self) :

        def get_forwarded_url(self) :
            
            self.login_to_website()
            time.sleep(3)
            current_url = self.driver.current_url
            return current_url
        
        def set_driver_to_forwarded_url(self): 

            new_url = get_forwarded_url(self)    
            self.driver = self.driver.get(new_url)      
            time.sleep(3) 

        def read_text_forwarded_website(self):
            
            set_driver_to_forwarded_url(self)
            text_output = self.driver.find_element(By.CLASS_NAME, "d-flex align-items-center justify-content-center display-4 mb-4 ErgebnisText")
            return text_output

        read_text_forwarded_website(self)


x = get_strava_data(path = r"C:\Users\norma\chromedriver.exe",
                website= 'https://mein-laborergebnis.de',
                pw = ''
                 )

print(x.get_text_from_website())

   