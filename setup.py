#!/usr/bin/env python

from setuptools import setup

setup(
	name = "wciwt",
	version = "0.2",
	description = "wciwt is a command line tool which makes it easier to find your favorite TV shows and movies in India. It currently supports Netflix, Prime Video and Hotstar.",
	author = "Ajay",
	author_email = "ajaymkatte95@gmail.com",
	packages = ["wciwt"],
	download_url = "https://github.com/howdyauthors/wciwt",
	entry_points = {
		'console_scripts': [
			'wciwt = wciwt:wciwt'
		],
	},
	install_requires = ["requests"]
)