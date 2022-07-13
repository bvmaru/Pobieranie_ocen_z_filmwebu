import bs4

exampleFile = open('testFile1.html', encoding='UTF-8')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
title = exampleSoup.find('title')

elems = exampleSoup.select('.poster__link')
elems1 = exampleSoup.select('.userRate__rate')
print(len(elems))
print(elems[5])
print(len(elems1))
print(elems1[5])

userRate__rate