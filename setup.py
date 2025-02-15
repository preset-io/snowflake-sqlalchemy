#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2019 Snowflake Computing Inc. All right reserved.
#

from codecs import open
from os import path

from setuptools import setup

THIS_DIR = path.dirname(path.realpath(__file__))

try:
    from generated_version import VERSION
except ImportError:
    from version import VERSION
version = '.'.join([str(v) for v in VERSION if v is not None])

with open(path.join(THIS_DIR, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='snowflake-sqlalchemy',
    version=version,
    description='Snowflake SQLAlchemy Dialect',
    long_description=long_description,
    author='Snowflake Computing, Inc',
    author_email='support@snowflake.net',
    license='Apache License, Version 2.0',
    url='https://www.snowflake.net/',
    keywords="Snowflake db database cloud analytics warehouse",
    download_url='https://www.snowflake.net/',

    install_requires=[
        'sqlalchemy<2.0.0,>=1.4.0',
        'snowflake-connector-python<3.0.0',  # Keep in sync with extras dependency
    ],
    packages=[
        'snowflake.sqlalchemy',
    ],
    package_dir={
        'snowflake.sqlalchemy': '.',
    },
    package_data={
        'snowflake.sqlalchemy': ['LICENSE.txt'],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'snowflake=snowflake.sqlalchemy:dialect',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',
        'Environment :: Other Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: OS Independent',

        'Programming Language :: SQL',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Topic :: Database',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    extras_require={
        'development': [
            'pytest',
            'pytest-cov',
            'pytest-rerunfailures',
            'pytest-timeout',
            'mock',
            'pytz',
            'numpy',
        ],
        # This is mostly for testing, but users might also want to install
        #  our connector with appropiate optional dependencies through this package
        'pandas': ['snowflake-connector-python[pandas]<3.0.0']  # Keep in sync with requirements
    },
)
