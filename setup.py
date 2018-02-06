from setuptools import setup

setup(
	name = 'CoinCommand',
	version = '0.1',
	py_modules=['CoinCommand'],
	install_requires=[
	'click',
	'requests'
	'tabulate'
	],
	entry_points='''
		[console_scripts]
		CoinCommand=CoinCommand:cli
	''',
	)
	
