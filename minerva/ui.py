import ui
import sys
import getpass

# Reads the user credentials
def get_user_credentials():

	#################################################
	# Gets the user credential to store in the user #
	#################################################
	if sys.stdin.isatty():
		# Gets the credentials from the user
		_mail = raw_input('Email? ')
		_pin = getpass.getpass(stream=sys.stderr)
		_cred = [_mail, _pin]

	else:
		# Gets the credentials from stdin
		_cred = sys.stdin.readlines()

		if _cred.size() != 2:
			print 'Error: Malformed input. Missing arguments.'
			exit()
			
	return _cred

def confirm_input(args):

	