
try:
	from setuptools import setup 
except:
	from disutils.core import core


dependencies=['docopt','mechanize','beautifulsoup4']

setup(

	name='minerva',
	version='0.0.1',
	description='A python interface to the aging minerva website.',
	long_description=open('README.md').read(),
	url='https://github.com/cadesalaberry/minerva',
	author='cadesalaberry',
	author_email='cadesalaberry@yahoo.com',
	install_requires=dependencies,
	packages=['minerva'],
	entry_points={
		'console_scripts': [
			'minerva=minerva.main:start'
		],
	},
	classifiers={
		'Development Status :: 1 - Alpha',
		'Intended Audience :: Developers',
		'NaturalLanguage :: English',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2.6',
	}
)
