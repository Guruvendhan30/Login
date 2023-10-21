from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
#options.add_argument('--headless=new')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/html/html_tables.asp")
sleep(2)

print(driver.find_element(By.XPATH, "/html/body").text)

driver.close()



