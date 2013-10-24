from os.path import expanduser
from os.path import exists
from os.path import join
from os import makedirs
import getpass
import sys

# Reads the user credentials
def get_user_credentials():

	"""Gets the user credentials from the commandline.

	Asks the user for his McGill email address and password.


	Args:
		None

	Returns:
		An array containing the user credentials. For example:
		
		['username','password']

		Notice that no checks for validity is applied to the input.
		For testing purposes, if not executed in a tty, the username
		and password are goign to be read from stdin.

		Example:

			minerva register 69 < credentials.txt

	Raises:
		IOError: An error occurred accessing the username file.
	"""

	if sys.stdin.isatty():
		# Gets the credentials from the userFile if it exists
		
		_mail = getusername()

		_pin = getpass.getpass(stream=sys.stderr)
		_cred = [_mail, _pin]

	else:
		# Gets the credentials from stdin
		_cred = sys.stdin.readlines()
		_cred = map(str.strip, _cred)

		print 'autologin\t:', _cred[0] 
		if len(_cred) != 2:
			print 'Error: Malformed input. Missing arguments.'
			exit()
			
	return _cred

def getusername():

	_userPath = expanduser("~/.minerva/")
	_userFile = join(_userPath, 'user')
	_mail = ""

	if not exists(_userFile):
		if not exists(_userPath):
			makedirs(_userPath)
		open(_userFile, 'w').close()

	userFile = open(_userFile, 'r+')

	_mailSaved = userFile.readline().strip()
	
	if '@' and '.' in _mailSaved:
		print 'Read\t:', _mailSaved
		_mail = _mailSaved
	else:
		_mail = raw_input('Email\t: ')

	if '.' in _mail and not '@' in _mail:
		_mail = _mail + '@mail.mcgill.ca';

	if _mail == _mailSaved:
		userFile.write(_mail)
	userFile.close()

	return _mail