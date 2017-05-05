#!/usr/bin/env python

from setuptools import setup, find_packages


PACKAGE = 'saferjson'

setup(
    name=PACKAGE,
    description=(
        'JSON parsing/serialization with safety and precision improvements.'
    ),
    version='0.1',
    author='Nathan Wilcox',
    author_email='nejucomo@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/{}'.format(PACKAGE),

    packages=find_packages(),
    install_requires=[
        'genty == 1.3.2',
        # 'mock == 2.0.0',
    ],

    entry_points={
        'console_scripts': [
            '{0} = {0}.check:main'.format(PACKAGE)
        ],
    }
)
