import os.path
from setuptools import setup, find_packages

NAME = 'myexamplelib'
VERSION = '0.1'

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
