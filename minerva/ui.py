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

	_userPath = expanduser("~/.minerva/")
	_userFile = join(_userPath, 'user')

	if sys.stdin.isatty():
		# Gets the credentials from the userFile if it exists
		
		try:
			with open(_userFile) as userFile:
				_mail = userFile.readline().strip()
				print 'Read\t:', _mail
		except IOError:
			if not exists(_userPath):
				makedirs(_userPath)

			userFile = open(_userFile, 'w')
			_mail = raw_input('Email?\t')
			userFile.write(_mail)

		userFile.close()

		_pin = getpass.getpass(stream=sys.stderr)
		_cred = [_mail, _pin]

	else:
		# Gets the credentials from stdin
		_cred = sys.stdin.readlines()
		print _cred
		if _cred.size() != 2:
			print 'Error: Malformed input. Missing arguments.'
			exit()
			
	return _cred