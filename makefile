default: install

build:
	python setup.py build --build-base=./build

install: setup.py
	python setup.py install --user

uninstall:
	pip uninstall minerva

reinstall: uninstall install