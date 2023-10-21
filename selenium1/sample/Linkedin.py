from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# import xlsxwriter
# from xlsxwriter import workbook, worksheet
# from lxml.objectify import element

# from idlelib.idle_test.test_colorizer import source

options=Options()
options.add_argument("--start-maximized")
driver=webdriver.Chrome(options=options)

import os

def loginLink(link,Usr_name,Pass_code):
    
    #url
    driver.get(link)
    time.sleep(2)
    
    #usrname
    Username=driver.find_element(By.ID,"username")
    Username.click()
    Username.send_keys(Usr_name)
    time.sleep(2)
    
    #pass
    Passcode=driver.find_element(By.ID,"password")
    Passcode.click()
    Passcode.send_keys(Pass_code)
    time.sleep(2)
    
    #signin
    Signin=driver.find_element(By.XPATH,"//button[@aria-label='Sign in']")
    Signin.click()
    time.sleep(15)
    
    #profileurl
    driver.get(profileurl)
    time.sleep(2)
    
    start=time.time()    
    #scroll the page
    initialscroll=0
    finalscroll=1000
    
    while True:
        driver.execute_script(f"window.scrollTo({initialscroll},{finalscroll})")
        initialscroll=finalscroll
        finalscroll+=1000
        time.sleep(2)
    
        end=time.time()
    
        if round(end-start)>20:
            break
    
    Sorc=driver.page_source
    soup=BeautifulSoup(Sorc,"lxml")
    time.sleep(5)
    
    introduction=soup.find('div',{'class':'mt2 relative'})
    time.sleep(5)
    # print(introduction)
    
    name_find=introduction.find("h1")
    name=name_find.get_text().strip()
    
    study_find=introduction.find('div',{'class':'text-body-medium break-words'})
    study=study_find.get_text().strip()
    
    college_n=introduction.find('div',{'tabindex':'-1'})
    college=college_n.get_text().strip()
    
    study_loc=introduction.find('span',{'class':'text-body-small inline t-black--light break-words'})
    loc=study_loc.get_text().strip()
    
    print("Name:",name,
          "\nStudies:",study,
          "\nCollege:",college,
          "\nLocation:",loc)
    
    experience=soup.find('div',{'class':'display-flex flex-column full-width align-self-center'})
    time.sleep(5)
    # print(experience)
    
    work=experience.find('div',{'class':'display-flex align-items-center mr1 t-bold'}).get_text().strip()
    
    company=experience.find('span',{'class':'t-14 t-normal'}).get_text().strip()
    
    compa_loc=experience.find('span',{'class':'t-14 t-normal'}).get_text().strip()
    
    print("Work:",work,
          "\ncompany:",company,
          "\nlocation:",compa_loc)  
    
    job=driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M17 6V5a3 ')]")
    job.click()
    time.sleep(3)
        
    # Job_all=driver.find_element(By.XPATH,"//a[@aria-label='Show all Recommended for you']//span[@class='artdeco-button__text'][normalize-space()='Show all']")
    # Job_all.click()
    # time.sleep(10)
    
    Job_src=driver.page_source
    job_soup=BeautifulSoup(Job_src,"lxml")
    time.sleep(5)
    print(job_soup)
    
    job_title=job_soup.find_all('a',{'class':'job-card-list__title'}).get_text().strip()
    print(job_title)
    
    Comp_name=job_soup.find('div',{'id':"ember395"}).get_text().strip()
    print(Comp_name)
    
    # Comp_loc=job_soup.find()
    
    # element_list=[]
    #
    # with xlsxwriter.Workbook('result.xlsx')as workbook:
    #     worksheet = workbook.add_worksheet()
    #
    #     for row_num, data in enumerate(element_list):
    #         worksheet.write_row(row_num,0,data)
    #
    # driver.close()
    
            
    
    

        
    
        
        
    
           
    
    
        
    
    
    
    
        
    
    
#cred
link="https://www.linkedin.com/login"
Usr_name="guruvendhan1@gmail.com"
Pass_code="guru2000"
profileurl="https://www.linkedin.com/in/ezhilan-K"    
    
loginLink(link,Usr_name,Pass_code)
    
    
    




url="https://www.linkedin.com/login"