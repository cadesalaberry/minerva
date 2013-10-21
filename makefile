default: install

install: setup.py
	python setup.py develop --user

uninstall:
	python setup.py develop -u --user