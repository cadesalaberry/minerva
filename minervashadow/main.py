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

from minervashadow import get_version
from docopt import docopt
import ui.cli as cli
import minerva


def interruptable(fn):
	"""Exits the program if Ctrl+C is pressed"""
	def wrapper(*args, **kwargs):
		try:
			fn(*args, **kwargs)
		except KeyboardInterrupt:
			print '\n\nExiting...\nHope to see you soon!'
			exit()
	return wrapper


@interruptable
def start():

	args = docopt(__doc__, version=get_version())
	validRequest = True

	credentials = cli.get_user_credentials()

	session = minerva.MinervaSession(credentials)

	if not args['login']:
		session.deal_with_request(args)

	session.logout()