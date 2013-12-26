[![McGill Logo](./assets/img/shadow-logo-transparent-big.png)](https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin "Minerva Webpage")



Minerva Shadow
=======

A python interface to the aging minervashadow website.


## Usage

Usage:

	minervashadow login
	minervashadow transcript
	minervashadow -h | --help
	minervashadow -v | --version

Examples:

	minervashadow login
	minervashadow transcript

Options:

	-h, --help     Show this screen.
	-v, --version  Print the current version.


## Installation


### Simple (with pip)

The package has not been submitted to the Python Package Index (PyPi) yet, but you will be able to install it using:

	pip install minervashadow


### Manual

The simplest way to install the package is using the makefile provided in the repository. Provifing you already have git installed:

	git clone https://github.com/cadesalaberry/minervashadow.git
	cd minervashadow
	make

And you are good to go ! you can then use the command-line client by typing it's name anywhere in the terminal:

	minervashadow


### Uninstallation

To remove the package, just run:

	make uninstall


## SOCS Server bug

If you want to install minervashadow on your SOCS server, you might run into the same issues I did, providing we don't have root privileges. In order to solve it, I just had to modify my **~/.bashrc** file to look like this:

	# .bashrc

	# Source global definitions
	if [ -f /usr/socs/Profile ]; then
	        . /usr/socs/Profile
	fi

	# User specific aliases and functions
	export PYTHONPATH=$HOME/.local/lib/python2.7/site-packages:$PYTHONPATH
	export PATH=$HOME/.local/bin:$PATH


The two last lines are the most important.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/cadesalaberry/minervashadow/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

