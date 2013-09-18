import sys
import getpass
from os.path import expanduser


# Reads the user credentials
def get_user_credentials():

	#################################################
	# Gets the user credential to store in the user #
	#################################################

	_userPath = expanduser("~") + '/.minerva/user'

	if sys.stdin.isatty():
		# Gets the credentials from the userFile if it exists
		
		try:
			with open(_userPath) as userFile:
				_mail = userFile.readline().strip()
				print 'Read:', _mail
				pass
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