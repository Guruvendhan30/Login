from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Thread
from threading import Event
import time

options = Options()
#options.add_argument('--headless=new')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

import os

def startbot(FirstName,LastName,Email,Password,ConfirmPassword,url):
  
    driver.get(url)
    
    #login home page
    # driver.find_elements_by_class_name("ico-login").click()
    #account creation page
    register=driver.find_element(By.CLASS_NAME,"ico-register")
    register.click()
    time.sleep(2)
    
    #account creation
    #gender
    
    ID=driver.find_element(By.ID,"gender-male")
    ID.click()
    time.sleep(2)
    
    #fname
    Fname=driver.find_element(By.ID,"FirstName")
    Fname.click()
    Fname.send_keys(FirstName)
    time.sleep(2)
    
    #Sname
    Lname=driver.find_element(By.ID,"LastName")
    Lname.click()
    Lname.send_keys(LastName)
    time.sleep(2)
    
    #email
    E_mail=driver.find_element(By.ID,"Email")
    E_mail.click()
    E_mail.send_keys(Email)
    time.sleep(2)
    
    #pass
    Pass=driver.find_element(By.ID,"Password")
    Pass.click()
    Pass.send_keys(Password)
    time.sleep(2)
    
    #confirmpass
    Cpass=driver.find_element(By.ID,"ConfirmPassword")
    Cpass.click()
    Cpass.send_keys(ConfirmPassword)
    time.sleep(2)
    
    #register
    Reg=driver.find_element(By.ID,"register-button")
    Reg.click()
    time.sleep(5)
    
    cont=driver.find_element(By.CLASS_NAME,"buttons")
    cont.click()
#credentials
FirstName="Guru"
LastName="Vendhan"
Email="gv38@gmail.com"
Password="Guru@3003"
ConfirmPassword="Guru@3003"

#url
url="https://demowebshop.tricentis.com/"

startbot(FirstName,LastName,Email,Password,ConfirmPassword,url)

