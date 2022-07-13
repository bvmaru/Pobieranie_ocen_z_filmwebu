from cmath import inf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# def loginUser():
#     while True:
#         if 



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.implicitly_wait(60) # seconds
driver.get('http://filmweb.pl/login')

try:
    element = WebDriverWait(driver, inf).until_not(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
finally:
    driver.get('http://filmweb.pl/user/test_test_3690/films?page=2')
    time.sleep(15)
    try:
        rates = driver.find_elements(By.CLASS_NAME, 'userRate__rate')
        first_titles = driver.find_elements(By.CLASS_NAME, 'preview__link')
        second_titles = driver.find_elements(By.CLASS_NAME, 'preview__originalTitle')
        
        for title in second_titles:
            print(title)

        for i in range(len(rates)):
            if second_titles[i] != None:
                print(second_titles[i].text +" "+rates[i].text)
            else:
                print(first_titles[i].text +" "+rates[i].text)


        # page = driver.page_source
        # testFile = open('testFileSelenium.html', 'wb')
        # testFile.write(page)
        # testFile.close()

    except:
        print('Nie udało się znaleźć elementu wraz z podaną nazwą klasy.')




#      test_test_3690
#      Haslotestowedofilmwebu1