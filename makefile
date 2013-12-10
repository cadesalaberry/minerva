default: user-install

remove: user-uninstall

install: setup.py
	python setup.py install

uninstall:
	python setup.py develop -u
	python setup.py clean --all

	if [ -d "minervashadow.egg-info" ];	then rm -r minervashadow.egg-info; fi
	if [ -d "dist" ];	then rm -r dist; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi

user-install: setup.py
	python setup.py install --user

user-uninstall:
	python setup.py develop -u --user
	python setup.py clean --all
	
	if [ -d "minervashadow.egg-info" ];	then rm -r minervashadow.egg-info; fi
	if [ -d "dist" ];	then rm -r dist; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi
