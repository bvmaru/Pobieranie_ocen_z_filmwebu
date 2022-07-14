from cmath import inf
from genericpath import exists
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

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
        date_added = packs[i].find_element(By.CLASS_NAME, 'voteCommentBox__date')
        movie = {
            'Title': Title.text,
            'Orig. title': orig_title.text,
            'Year': year.text,
            'Rate': rate.text,
            'Fav': fav,
            'Date added': date_added.text,
        }
        movie_sub_list.append(movie)
    return movie_sub_list

