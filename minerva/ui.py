import sys
import getpass
from os.path import expanduser


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

	_userPath = expanduser("~") + '/.minerva/user'

	if sys.stdin.isatty():
		# Gets the credentials from the userFile if it exists
		
		try:
			with open(_userPath) as userFile:
				_mail = userFile.readline().strip()
				print 'Read : ', _mail
		except IOError:
			userFile = open(_userPath, 'w')
			_mail = raw_input('Email? ')
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

def get_current_semester():

	return '201401'
