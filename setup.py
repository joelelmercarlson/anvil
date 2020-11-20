# -*- coding:utf-8 -*-

"""
setup.py -- Package and distributions management.
"""
from setuptools import setup, find_packages

with open('README.md') as stream:
    README = stream.read()

with open('LICENSE.md') as stream:
    LICENSE = stream.read()

setup(
    name='Anvil',
    version='2020.11.20',
    description='ImageFactory module',
    long_description=README,
    author='Joel E Carlson',
    author_email='joel.elmer.carlson@gmail.com',
    url='https://github.com/joelelmercarlson/anvil',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
