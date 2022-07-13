import requests


# payload = {
#     'username' : 'test_test_3690',
#     'current-password' : 'Haslotestowedofilmwebu1',
# }

# s = requests.Session()
# s.post('https://www.filmweb.pl/login?error=default', data = payload)
# s.get('https://www.filmweb.pl/user/test_test_3690/films')

# testFile = open('testFile1.html', 'wb')
# for chunk in s.get('https://www.filmweb.pl/user/test_test_3690/films').iter_content(100000):
#     testFile.write(chunk)

# testFile.close()

cookies = {'cookie':'mousestats_vi=635ac24f30ab70904304; _ga_614EWCM3W6=GS1.1.1604275548.1.0.1604275558.0; _ga=GA1.2.752062496.1587417435; fupi=38; __gfp_64b=WD0sD7xMG2S1cTAoOkl1Gn0henC52pIvNMvtQZN3_2n.P7|1564173199; canProfile=true_1634383636073; onBoardingShownCRITIC_RATING=1; _hsmid=News_145901; didomi_token=eyJ1c2VyX2lkIjoiMTc0NWE3ZGEtZjZlNS02NTNkLTg2NGMtZjMyOGJmM2Q4YjAwIiwiY3JlYXRlZCI6IjIwMjItMDYtMjhUMjE6Mjc6MjguNzg2WiIsInVwZGF0ZWQiOiIyMDIyLTA2LTI4VDIxOjI3OjI4Ljc4NloiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6ZGlkb21pIiwiYzpob3RqYXIiLCJjOmFkb2NlYW4iLCJjOmFudGlhZGJsby1lekN4a2dxbiIsImM6YW1uZXQtUEE0cWZ6anoiLCJjOmVmaWdlbmNlLWl3OHdUeEdUIiwiYzpoYXZhc21lZGktbWUyekt4SkoiLCJjOnBlcmZvcm1hbmMtaENFeFJ5bVYiLCJjOnZhbHVlbWVkaS1OelJSRWhkTCIsImM6d2F2ZW1ha2VyLXdCdFRHemFaIiwiYzp3YXl0b2dyb3ctUmFCRGszVzQiLCJjOm9tZHNwem8tQ3pQeDZ0UFYiLCJjOmFydGVnZW5jZS1aaGprQkhHbSIsImM6bWF0b21vLU4zZ2szN2FUIl19LCJwdXJwb3NlcyI6eyJkaXNhYmxlZCI6WyJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIiwiZ2VvbG9jYXRpb25fZGF0YSJdfSwidmVuZG9yc19saSI6eyJlbmFibGVkIjpbImdvb2dsZSJdfSwidmVyc2lvbiI6MiwiYWMiOiJBQUFBLkFBQUEifQ==; euconsent-v2=CPbRq0APbRq0AAHABBENCVCgAAAAAAAAAB5YAAARrAJMNW4gC7EscGTaMIoUQIwrCQ6gUAFFAMLRFYQOrgp2VwE-oIWACAVARgRAgxBRgwCAAQCAJCIgJADwQCIAiAQAAgAVAIQAEbAILACwMAgAFANCxAigCECQgyICI5TAgIkSignsrEEoO9jTCEOssAKBR_RUICJQAgWBkJCwcxwBICXCyQLMUL5ACMEKAUAA.YAAAAAAAAAAA; _art_fbc_accessToken=RUFBQUFOTk9RQnAwQkFDWkNrUTVDeUNBemFtSEVFQUhrQlpDY3M2bUpDU2VQeUFvS2VMSUkyWGpHb1RkM1A1RmNJTklQWFRDMnNFWUdwYUV3dHJiQno4NUZKdkhaQzNqYXk5UjNya05zeDRrQ3pPWFhYMm55elpBM2ZoSUlQZFhNYnl5dDlSR0Q1MENvUkg3ajJ6NXE0OXl0WkFHMldYVHJ1QkVUOENENkpUcUthajB4QTRMNjU=; ws_ad=["d2VsY29tZVNjcmVlbkpTT04ucGxfUEw6NTBDVzlOVjJHWQ=="]; JWT=eyJhbGciOiJIUzI1NiJ9.eyJwZXJtaXNzaW9ucyI6W10sImNzcmYiOiIwam5XL242cEg2MERDeXJLRFNwcW93PT0iLCJ1c2VySWQiOjQyMzM2NzAsInN1YiI6Ik1hcmNlbG8zNjkiLCJleHAiOjE2NTc2MzI3MDMsImlhdCI6MTY1NzYzMTgwM30.oUU8utkameqEfimwN06qLyVD0ybCSNxWU__mC2Vx1cI; XSRF-TOKEN=0jnW/n6pH60DCyrKDSpqow==; _artuser_prm=aVMrNkdibVdlVUFoT3Z2YUlUdVBaZz09OmR3cTRZVVVSc212bHNEdVpwZkVjdWc9PQ; _fwuser_sessionId=WNwHlu0HyY6oZtA/H7Ozs7Pohubwb4PACThRlg+m02GKirU8pdKyfS58UWnuSU50g0uYJnSqcNyC3e5aSLYGTg==; _fwuser_token=jHDQwjvOyePZFYFXR4bH-0aw4sDds2jsVPc30aYB; _fwuser_logged=105'}

r = requests.get('https://www.filmweb.pl/user/Marcelo369/films?page=16', cookies=cookies)
testFile = open('testFile1.html', 'wb')
for chunk in r.iter_content(100000):
    testFile.write(chunk)

testFile.close()