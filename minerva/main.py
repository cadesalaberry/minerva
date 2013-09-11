#!/usr/bin/env python
"""
Usage:
	minerva register <class_crn>...
	minerva transcript
	minerva check <class_crn>
	minerva search <class_name>
	minerva -h | --help
	minerva -v | --version

Examples:
	minerva register 6969
	minerva transcript
	minerva check 321
	minerva search ecse420

Options:
	-h, --help     Show this screen.
	-v --version   Print the current version.
"""

import ui
from minerva import __version__
from docopt import docopt

def start():
	
	version = ".".join(str(x) for x in __version__)
	args = docopt(__doc__, version=version)
	print(args)
	print ui.confirm_input(args)
	print ui.get_user_credentials()