try:
	from setuptools import setup 
except:
	from disutils.core import setup

import minervashadow


dependencies=['docopt','mechanize','beautifulsoup4']

setup(

	name='minervashadow',
	version=minervashadow.get_version(),
	description='A python interface to the aging minerva website.',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minervashadow',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies,
	packages=['minervashadow'],
	entry_points={
		'console_scripts': [
			'minervashadow=minervashadow:start'
		],
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'NaturalLanguage :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7'
	]
)
