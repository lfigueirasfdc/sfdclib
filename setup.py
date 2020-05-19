"""sfdclib_alt package setup"""

import textwrap
from setuptools import setup

setup(
    name='sfdclib_alt',
    version='0.1',
    author='Luis Figueira',
    author_email='lfigueira@salesforce.com',
    packages=['sfdclib_alt'],
    url='https://github.com/lfigueirasfdc/sfdclib',
    license='MIT',
    description=("SFDClib_alt is a fork of rbauction/sfdclib, to include the ability to retrieve packaged metadata"),
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    package_data={'': ['LICENSE']},
    package_dir={'sfdclib_alt': 'sfdclib_alt'},
    install_requires=[
        'requests[security]'
    ],
    keywords="python salesforce salesforce.com metadata tooling api",
    classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)
