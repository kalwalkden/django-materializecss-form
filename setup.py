#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import materializecssform

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name='django-materializecss-form',

    version=materializecssform.__version__,

    packages=find_packages(),

    author="Kal Walkden",

    author_email="kal@walkden.us",

    description="A simple Django form template tag to work with Materializecss",
    long_description=long_description,
    long_description_content_type="text/markdown",

    include_package_data=True,

    url='https://github.com/kalwalkden/django-materializecss-form',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],

    license="MIT",

    zip_safe=False
)
