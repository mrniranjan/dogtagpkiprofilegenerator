#!/usr/bin/python
#
# Copyright (C) 2016 sssd-qe contributors.
#
from setuptools import setup

REQUIRES = [
        'lxml'
        ]

setup_args = dict(
        name = 'pkiprofilegen',
        version = '0.1',
        description = 'PKI Profile generator',
        author = u'Niranjan',
        url = 'http://gitlab.cee.redhat.com/pkiprofilegen',
        packages = [
            'pkiprofilegen',
        ],
        package_data={'':['LICENSE']},
        install_requires=REQUIRES,
        license='GNU GPL v3.0',
        entry_points = {
                'console_scripts': [
                    'pkiprofilexmlgen = pkiprofilegen.pkiprofilecli:main' ]
                    },
        classifiers=(
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            ),
        )

if __name__ == '__main__':
    setup(**setup_args)
