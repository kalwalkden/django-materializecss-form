#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
import materializecssform
 
setup(
 
    name='django-materializecss-form',
 
    version=materializecssform.__version__,
 
    packages=find_packages(),
 
    author="Florent CLAPIÉ",
 
    author_email="clapie.florent@gmail.com",
 
    description="A simple Django form template tag to work with Materializecss",

    long_description=open('README.rst').read(),
 
    # install_requires= ,
 
    include_package_data=True,
 
    url='https://github.com/florent1933/django-materializecss-form',
 
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Documentation :: Sphinx",
    ],
 
    license="MIT",
)
