default: user-install

remove: user-uninstall

install: setup.py
	python setup.py develop

uninstall:
	python setup.py develop -u

user-install: setup.py
	python setup.py develop --user

user-uninstall:
	python setup.py develop -u --user
	python setup.py clean --all
	
	if [ -d "minervashadow.egg-info" ];	then rm -r minervashadow.egg-info; fi
	if [ -d "dist" ];	then rm -r dist; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi