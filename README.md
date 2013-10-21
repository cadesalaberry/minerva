minerva
=======

A python interface to the aging minerva website.

[![McGill Logo](./assets/mcgill-logo-transparent.png)](https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin "Minerva Webpage")


# Usage

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


# Installation

### Simple (with pip)

The package has not been submitted to the Python Package Index (PyPi) yet, but you will be able to install it using:

	pip install minerva


### Manual
The simplest way to install the package is using the makefile provided in the repository. Provifing you already have git installed:

	git clone https://github.com/cadesalaberry/minerga.git
	cd minerva
	make

And you are good to go ! you can then use the command-line client by typing it's name anywhere in the terminal:

	minerva


### Uninstallation

To remove the package, just run:

	make uninstall


# SOCS Server bug

If you want to install minerva on your SOCS server, you might run into the same issues I did, providing we don't have root privileges. In order to solve it, I just had to modify my **~/.bashrc** file to look like this:

	># .bashrc

	# Source global definitions
	if [ -f /usr/socs/Profile ]; then
	        . /usr/socs/Profile
	fi

	# User specific aliases and functions
	**export PYTHONPATH=$HOME/.local/lib/python2.7/site-packages:$PYTHONPATH**
	**export PATH=$HOME/.local/bin:$PATH**

The two last lines are the most important.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/cadesalaberry/minerva/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

