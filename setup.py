from setuptools import setup

setup(
	name = 'CoinCommand',
	version = '0.3',
	py_modules=['CoinCommand'],
	install_requires=[
	'click',
	'requests'
	],
	entry_points='''
		[console_scripts]
		CoinCommand=CoinCommand:cli
	''',
	)
	
