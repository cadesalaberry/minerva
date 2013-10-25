from os import makedirs
from os import path
import getpass
import sys

# Reads the user credentials
def get_user_credentials():

	"""Gets the user credentials from the commandline.

	Asks the user for his McGill email address and password.


	Args:
		None

	Returns:
		An array containing the user credentials.

		Notice that no checks for validity is applied to the input.
		For testing purposes, if not executed in a tty, the username
		and password are goign to be read from stdin.

		Example:

			['username','password']

	Raises:
		IOError: An error occurred accessing the username file.
	"""

	if sys.stdin.isatty():
		# Gets the credentials from the userFile if it exists
		_mail = getusername()
		_pass = getpass.getpass(stream=sys.stderr)
		_cred = [_mail, _pass]

	else:
		# Gets the credentials from stdin
		_cred = sys.stdin.readlines()
		_cred = map(str.strip, _cred)

		print 'autologin\t:', _cred[0] 
		if len(_cred) != 2:
			print 'Error: Malformed input. Missing arguments.'
			exit()
			
	return _cred


def getusername(reset=False):

	"""	Gets the username either from the commandline,
		either from the user file (in ~/.minerva/).

	Asks the user for his McGill email address if no previous session
	has been stored, and save the session in the user file.


	Args:
		None

	Returns:
		A string containing the user email.

		Example:

			'john.doe@mail.mcgill.ca'

	Raises:
		None
	"""

	_mailSaved = savedusername()
	_mail = ""
	
	if reset or ('@' and '.' in _mailSaved):
		print 'Read\t:', _mailSaved
		_mail = _mailSaved
	else:
		_mail = raw_input('Email\t: ')

		# Auto-completes the username if domain missing 
		if '.' in _mail and not '@' in _mail:
			_mail = _mail + '@mail.mcgill.ca'

	# Stores the email to the user file
	if _mail != _mailSaved:
		savedusername(_mail)

	return _mail

"""

"""
def savedusername(username=""):

	_userPath = path.expanduser("~/.minerva/")
	_userFile = path.join(_userPath, 'user')

	if not path.exists(_userPath):
		path.makedirs(_userPath)

	if not path.exists(_userFile):
		open(_userFile, 'w').close()

	if username == "":
		userFile = open(_userFile, 'r+')
		username = userFile.readline().strip()
		userFile.close()
	else:
		userFile = open(_userFile, 'w+')
		userFile.write(username)
		userFile.close()

	return username