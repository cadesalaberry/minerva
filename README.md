[![McGill Logo](./assets/img/shadow-logo-transparent-big.png)](https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin "Minerva Webpage")



minervashadow
=======

A python interface to the aging Minerva website.


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

If you just want to run the package without prior installation, (provided you already have install the depedencies) run:

	git clone https://github.com/cadesalaberry/minervashadow.git
	python minervashadow


### Simple

	pip install minervashadow

If you prefer not to use Pypi, or want to get the latest cutting-edge version, you can pull directly from github:

	pip install git+https://github.com/cadesalaberry/minervashadow


### Uninstallation

To remove the package, just run:

	pip uninstall minervashadow


### SOCS Server bug

In installing minervashadow on your SOCS server, you might run into the same issues I did:

	minervashado: command not found

To solve it, I just had to modify my **~/.bashrc** file to look like this:

	# .bashrc

	# Source global definitions
	if [ -f /usr/socs/Profile ]; then
	        . /usr/socs/Profile
	fi

	# User specific aliases and functions
	export PYTHONPATH=$HOME/.local/lib/python2.7/site-packages:$PYTHONPATH
	export PATH=$HOME/.local/bin:$PATH


The two last lines add the python packages folder to the PATH.


## Contribute

To contribute do not hesitate to send me pull requests !


### Dev Environment

To help on the development of the app you can setup your dev environment as follow:

	git clone https://github.com/cadesalaberry/minervashadow.git
	cd minervashadow
	python setup.py develop

And you are good to go !


## Future

The future of this package is uncertain for now, but here is the planning I had for it on the short term if you are interested:

https://github.com/cadesalaberry/minervashadow/issues/milestones