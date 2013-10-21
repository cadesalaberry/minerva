#!/usr/bin/env python
"""
Usage:
	minerva login
	minerva register <class_crns>...
	minerva drop <class_crn>
	minerva transcript
	minerva check <class_crn>
	minerva search <class_name> | <class_crn>
	minerva list [all]
	minerva -h | --help
	minerva -v | --version

Examples:
	minerva register 6969
	minerva transcript
	minerva check 321
	minerva search ecse420

Options:
	-h, --help     Show this screen.
	-v, --version  Print the current version.
"""

import ui
from docopt import docopt
from minerva import MinervaSession

def start():

	try:
		start_minerva()
	except KeyboardInterrupt:
		print '\n\nExiting...\nHope to see you soon!'


def start_minerva():
	
	args = docopt(__doc__, version='0.0.1')
	validRequest = True

	if args['register']:
		if len(args['<class_crns>']) < 10:
			print 'Trying to register to:', args['<class_crns>']
		else:
			print 'Error: Too many CRNs specified.'
			validRequest = False


	if validRequest:

		credentials = ui.get_user_credentials()

		session = MinervaSession(credentials)

		session.login()
		
		if not args['login']:
			session.deal_with_request(args)

		session.logout()
		print 'Logged out !'

	else:
		print 'Error: Invalid input.'
		print 'try "minerva -h" to display the help screen.'
		print 'Exiting...'