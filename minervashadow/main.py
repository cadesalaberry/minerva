#!/usr/bin/env python
"""
Usage:
	minervashadow login
	minervashadow register <class_crns>...
	minervashadow drop <class_crn>
	minervashadow transcript
	minervashadow check <class_crn>
	minervashadow search <class_name> | <class_crn>
	minervashadow list [all]
	minervashadow -h | --help
	minervashadow -v | --version

Examples:
	minervashadow register 6969
	minervashadow transcript
	minervashadow check 321
	minervashadow search ecse420

Options:
	-h, --help     Show this screen.
	-v, --version  Print the current version.
"""

from minervashadow import MinervaSession
from docopt import docopt
import ui


def start():

	try:
		handled_exit()
	except KeyboardInterrupt:
		print '\n\nExiting...\nHope to see you soon!'


def handled_exit():
	
	args = docopt(__doc__, version='0.0.2')
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

		if not args['login']:
			session.login()

		session.deal_with_request(args)

		session.logout()
		print 'Logged out !'

	else:
		print 'Error: Invalid input.'
		print 'try "minervashadow -h" to display the help screen.'
		print 'Exiting...'