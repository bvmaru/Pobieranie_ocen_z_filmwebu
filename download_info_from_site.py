from cmath import inf
from genericpath import exists
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re

def download_info_from_site(driver):
    movie_sub_list = []
    packs = driver.find_elements(By.CLASS_NAME, 'myVoteBox__mainBox')
    print(len(packs))
    for i in range(len(packs)):
        Title = packs[i].find_element(By.CLASS_NAME, 'preview__link')
        if len(packs[i].find_elements(By.CLASS_NAME, 'preview__originalTitle')) == 0:
                orig_title = Title
        else:
            orig_title = packs[i].find_element(By.CLASS_NAME, 'preview__originalTitle')
        year = packs[i].find_element(By.CLASS_NAME, 'preview__year')
        rate = packs[i].find_element(By.CLASS_NAME, 'userRate__rate')
        if len(packs[i].find_elements(By.CLASS_NAME, 'favourite__icon--active')) == 0:
            fav = 0
        else:
            fav = 1
        if len(packs[i].find_elements(By.CLASS_NAME, 'voteCommentText__label')) == 0:
            review = " "
        else:
            review = packs[i].find_element(By.CLASS_NAME, 'voteCommentText__label').text
        date_added = packs[i].find_element(By.CLASS_NAME, 'voteCommentBox__date')
        date_dictionary = {
            'stycznia' : '01',
            'lutego' : '02',
            'marca' : '03',
            'kwietnia' : '04',
            'maja' : '05',
            'czerwca' : '06',
            'lipca' : '07',
            'sierpnia' : '08',
            'września' : '09',
            'października' : '10',
            'listopada' : '11',
            'grudnia' : '12',
        }
        cap_date = re.compile(r'(\d?) (\w+) (\d{4})')
        wd = cap_date.search(date_added.text)
        wf = wd.group(3) +"-"+date_dictionary[wd.group(2)]+"-"+wd.group(1)
        if review == 'Dodaj komentarz':
            review = ''

        movie = {
            'Title PL': Title.text,
            'Title': orig_title.text,
            'Year': year.text,
            'Rating10': rate.text,
            'Fav': fav,
            'Review': review,
            'WatchedDate': wf,
        }
        movie_sub_list.append(movie) 
    return movie_sub_list


