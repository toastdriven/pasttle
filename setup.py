#!/usr/bin/env python
#
# -*- mode:python; sh-basic-offset:4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim:set tabstop=4 softtabstop=4 expandtab shiftwidth=4 fileencoding=utf-8:
#

import os
import sys
from setuptools import setup

extra = {
    'install_requires': [
        'distribute',
        'bottle>=0.9',
        'Pygments',
        'SQLAlchemy',
        'bottle-sqlalchemy',
        'bottle-sqlite',
    ]
}

if sys.version_info >= (3,):
    extra['use_2to3'] = True

readme = os.path.join(os.path.dirname(sys.argv[0]), 'README.markdown')


setup(
    name='pasttle',
    packages=[
        'pasttle',
    ],
    version='0.6.4',
    url='http://github.com/thekad/pasttle/',
    description='Simple pastebin on top of bottle.',
    author='Jorge Gallegos',
    author_email='kad@blegh.net',
    license='MIT',
    platforms='any',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pasttle-server.py=pasttle.pasttled:main'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['pastebin', 'web', 'paste', 'bottlepy'],
    long_description=open(readme).read(),
    **extra
)
