from cmath import inf
from genericpath import exists
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = (r"C:\Users\Marcel\Desktop\copy\chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.get('http://filmweb.pl/user/test_test_3690/films')
time.sleep(5)
for i in range(len(driver.find_elements(By.CLASS_NAME, 'userRate__favourite favourite'))):
    print(i)
