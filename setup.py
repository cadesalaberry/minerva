
try:
	from setuptools import setup 
except:
	from disutils.core import core


dependencies=['docopt','mechanize','beautifulsoup4']

setup(

	name='minervashadow',
	version='0.0.2',
	description='A python interface to the aging minerva website.',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minervashadow',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies,
	packages=['minerva'],
	entry_points={
		'console_scripts': [
			'minervashadow=minervashadow.main:start'
		],
	},
	classifiers={
		'Development Status :: 2 - Alpha',
		'Intended Audience :: Developers',
		'NaturalLanguage :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2.6',
	}
)
