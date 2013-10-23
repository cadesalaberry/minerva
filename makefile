default: install

install: setup.py
	python setup.py develop --user

uninstall:
	python setup.py develop -u --user
	python setup.py clean --all
	
	if [ -d "*.egg-info" ];	then rm -r *.egg-info; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi