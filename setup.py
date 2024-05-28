from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aicl/__init__.py
from aicl import __version__ as version

setup(
	name="aicl",
	version=version,
	description="Web Application for AICL , intergrated with ERPNEXT",
	author="Angalia Investment Consortium Limited",
	author_email="businessdevelopment@aicl.co.tz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
