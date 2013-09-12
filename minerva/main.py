#!/usr/bin/env python
"""
Usage:
	minerva register <class_crn>...
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
	-v, --version   Print the current version.
"""

import ui
from docopt import docopt

def start():
	
	args = docopt(__doc__, version='0.0.1')
	#print(args)

	ui.confirm_input(args)
	
	print ui.get_user_credentials()