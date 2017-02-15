import os
from setuptools import find_packages
from setuptools import setup
import re

setup(
	name='hmmvis',
	version = '0.1',
	description='hmmvis - HMM hit visualization',
	url = 'http://github.com/philippmuench/hmmvis',
	author='Philipp C. Muench',
	author_email='pmu15@helmholtz-hzi.de',
	license='GNU General Public License, version 3 (GPL-3.0)',
	packages= ['hmmvis'],
	include_package_data = True,
	scripts = ['hmmvis/hmmvis'],
	zip_safe=False,
	install_requires = ["appdirs >= 1.4.0","biopython >= 1.68","cycler >= 0.10.0","matplotlib >= 2.0.0","numpy >= 1.12.0", "pandas >= 0.19.2", "scipy", "seaborn >=  0.7.1"])
