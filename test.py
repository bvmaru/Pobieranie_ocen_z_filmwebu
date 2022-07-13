from wsgiref.headers import Headers
import requests
from bs4 import BeautifulSoup as bs

loginurl = "https://www.filmweb.pl/login?error=default"
URL = 'https://www.filmweb.pl'
referer = 'https://www.filmweb.pl/login?error=bad.credentials'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'origin': URL,
    'referer': referer 
}

s = requests.session()

#csrf_token = s.get(URL).cookies['csrftoken']

login_payload = {
    'j_username' : 'test_test_3690',
    'j_password' : 'Haslotestowedofilmwebu1',
    #'csrfmiddlewaretoken' : csrf_token
}

login_req = s.post(loginurl, data = login_payload)

print(login_req.status_code)

cookies = login_req.cookies


r = requests.get('https://www.filmweb.pl/user/test_test_3690/films')
testFile = open('testFile1.html', 'wb')
for chunk in r.iter_content(100000):
    testFile.write(chunk)

testFile.close()

# with requests.session() as s:
#     s.post(loginurl, data=payload)
#     r = requests.get('https://www.filmweb.pl/user/test_test_3690/films?page=2')
#     testFile = open('testFile.html', 'wb')
#     for chunk in r.iter_content(100000):
#         testFile.write(chunk)

#     testFile.close()

#     print(r.text)