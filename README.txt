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

If you just want to run the package without prior installation, run:

	git clone https://github.com/cadesalaberry/minervashadow.git
	python minervashadow


### Simple

	pip install --user minervashadow

Or

	easy_install minervashadow


### Advanced

If you prefer not to use Pypi, or want to get the latest cutting-edge version, you can pull directly from github:

	pip install git+https://github.com/cadesalaberry/minervashadow

Or you can use the makefile included in the repository, provided you already have git installed:

	git clone https://github.com/cadesalaberry/minervashadow.git
	cd minervashadow
	make

And you are good to go !


### Uninstallation

To remove the package, just run:

	pip uninstall minervashadow

Or

	make uninstall

Depending on how you installed it.


### SOCS Server bug

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


## Contribute

To contribute do not hesitate to send me pull requests ! However when doing so, make sure you modify the less code possible, or the request would not be clear.


## Future

The future of this package is uncertain for now, but here is the planning I had for it on the short term if you are interested:

https://github.com/cadesalaberry/minervashadow/issues/milestones


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/cadesalaberry/minervashadow/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
