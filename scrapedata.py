userID = 'DI temkin'
pwd = 'GRG76r8T'
payload = {'Login_ID': 'DI temkin', 'Pwd': 'GRG76r8T', 'Page': '', 'Submit': 'Login'}
import requests
s = requests.Session()
r1 = s.get('https://www.hi-bid.com/security/login.asp')
r2 = s.post('https://www.hi-bid.com/security/login_action.asp', data=payload)
r3 = s.get('https://www.hi-bid.com/search/results.asp?ps=100&ap=1&o=price&desc=&ys=1860&ye=2013&sd=ALL')
