from cmath import inf
from genericpath import exists
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from download_info_from_site import *

PATH = (r"C:\Users\Marcel\Desktop\copy\chromedriver.exe")
movie_list = []
user_name = input('Padaj swoją nazwę użytkownika Filmwebu (pamiętaj o zachowaniu odpowidniej wielkości znaków):')
driver = webdriver.Chrome(PATH)
driver.get('http://filmweb.pl/login')
try:
    element = WebDriverWait(driver, inf).until_not(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
finally:
    nr_strony = 1
    while(True):
        driver.get('http://filmweb.pl/user/%s/films?page=%s' % (user_name, nr_strony))
        time.sleep(1)
        body = driver.find_element(By.CSS_SELECTOR, 'body')
        for i in range(15):
            time.sleep(0.5)
            body.send_keys(Keys.PAGE_DOWN)
        try:
            movie_list.extend(download_info_from_site(driver))        
        except:
            print('Coś poszło nie tak!')
        if len(driver.find_elements(By.CLASS_NAME, 'ico--arrowRight')) == 0:
            driver.quit()
            break
        else:
            nr_strony += 1

for el in movie_list:
    print(el)

print(len(movie_list))

#      test_test_3690
#      Haslotestowedofilmwebu1