from cmath import inf
from genericpath import exists
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = (r"C:\Users\Marcel\Desktop\copy\chromedriver.exe")
movie_list = []
driver = webdriver.Chrome(PATH)
driver.get('http://filmweb.pl/login')
try:
    element = WebDriverWait(driver, inf).until_not(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
finally:
    driver.get('http://filmweb.pl/user/test_test_3690/films?page=1')
    time.sleep(5)
    try:
        packs = driver.find_elements(By.CLASS_NAME, 'myVoteBox__mainBox')
        first_titles = driver.find_elements(By.CLASS_NAME, 'preview__link')
        second_titles = driver.find_elements(By.CLASS_NAME, 'preview__originalTitle')
        print(len(packs))
        for i in range(len(packs)):
            Title = packs[i].find_element(By.CLASS_NAME, 'preview__link')
            if len(packs[i].find_elements(By.CLASS_NAME, 'preview__originalTitle')) == 0:
                orig_title = Title
            else:
                orig_title = packs[i].find_element(By.CLASS_NAME, 'preview__originalTitle')

            year = packs[i].find_element(By.CLASS_NAME, 'preview__year')
            rate = packs[i].find_element(By.CLASS_NAME, 'userRate__rate')
            #fav1 = packs[i].find_element(By.CLASS_NAME, 'userRate__favourite favourite')
            # if len(fav1.find_elements(By.CLASS_NAME, 'favourite__icon ico favourite__icon--active')) == 0:
            #     fav = 0
            # else:
            #     fav = 1
            fav = 1
            date_added = packs[i].find_element(By.CLASS_NAME, 'voteCommentBox__date')
            movie = {
                'title': Title.text,
                'orig_title': orig_title.text,
                'year': year.text,
                'rate': rate.text,
                'fav': fav,
                'date_added': date_added.text,
            }
            movie_list.append(movie)
            


        # for i in range(len(rates)):
        #     if second_titles[i] != None:
        #         print(second_titles[i].text +" "+rates[i].text)
        #     else:
        #         print(first_titles[i].text +" "+rates[i].text)


        # page = driver.page_source
        # testFile = open('testFileSelenium.html', 'wb')
        # testFile.write(page)
        # testFile.close()

    except:
        print('Coś poszło nie tak!')

for el in movie_list:
    print(el)

#      test_test_3690
#      Haslotestowedofilmwebu1