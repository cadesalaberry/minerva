default: user-install

remove: user-uninstall

install: setup.py
	python setup.py install --record files.txt

uninstall:
	python setup.py clean --all
	cat files.txt | xargs rm -rf

	if [ -d "minervashadow.egg-info" ];	then rm -r minervashadow.egg-info; fi
	if [ -d "dist" ];	then rm -r dist; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi

user-install: setup.py
	python setup.py install --user --record files.txt

user-uninstall:
	python setup.py clean --all
	cat files.txt | xargs rm -rf

	if [ -d "minervashadow.egg-info" ];	then rm -r minervashadow.egg-info; fi
	if [ -d "dist" ];	then rm -r dist; fi
	if [ -d "~/.minerva" ]; then rm -r ~/.minerva; fi

test:
	python setup.py test
