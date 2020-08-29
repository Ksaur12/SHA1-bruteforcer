#!usr/bin/python3
#Made by Ksaur12

from urllib.request import urlopen
from termcolor import colored
import hashlib

print('''For bruteforcing from online password list,TYPE 1
For bruteforcing from offline password list,TYPE 2''')

choice = input('Enter 1 or 2: ')

if choice == '1' :
	hashWord = input('Enter SHA1 hash: ')
	print('\nPassword list URL example = https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt\n')
	url = input('Enter URL(see upper line): ')
	
	passlist = str(urlopen(url).read(), 'utf-8')
	for password in passlist.split('\n'):
		passhash = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
		if passhash == hashWord:
			print(colored('\nPassword found: ' + password, 'green'))
			exit()
		else:
			print(colored(password + ' is incorrect', 'red'))
			
elif choice == '2' :
	hashWord = input('Enter sha1 hash: ')
	file = input('Enter name of password file: ')
	passlist = open(file)     #urlopen()
	for password in passlist:
		password = password.strip()
		passhash = hashlib.sha1(password.encode()).hexdigest()
		if passhash == hashWord:
			print(colored('\nPassword found: ' + password, 'green'))
			exit()
		else:
			print(colored(password + ' is incorrect', 'red'))
			
else:
	print('invalid')