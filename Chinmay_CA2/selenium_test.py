from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--disable-features=VizDisplayCompositor")

driver = webdriver.Chrome(options=options)

# open the form
driver.get("file:///C:/Users/ASUS/Desktop/College/Sem6/DevOps/Chinmay_CA2/index.html")
time.sleep(20)

# fill form
driver.find_element(By.ID,"name").send_keys("Chinmay")

driver.find_element(By.ID,"email").send_keys("chinu@gmail.com")

driver.find_element(By.ID,"course").send_keys("Web Development")

driver.find_element(By.ID,"instructor").send_keys("Prof. Sharma")

driver.find_element(By.ID,"rating").send_keys("Excellent")

time.sleep(10)

# submit form
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(30)

driver.quit()