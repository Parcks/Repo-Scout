#!/usr/bin/env python
"""
Repo Scout
Copyright (C) 2017  JValck - Setarit

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Setarit - parcks[at]setarit.com
"""
from setuptools import setup, find_packages

install_requires = [
    'mock==2.0.0',
    'requests==2.20.0',
]

setup(
    name='Repo Scout',
    version='1.0.0',
    description="Searches for a file in a VCS",
    long_description=open('README.rst').read(),
    author="Setarit",
    author_email='parcks@setarit.com',
    maintainer='JValck',
    maintainer_email='parcks@setarit.com',
    url='https://github.com/Parcks/Repo-Scout',
    packages=find_packages(),
    install_requires=install_requires,
    license="GPLv2",
    keywords='Parcks API Scout Find Repository',
    entry_points={
        'console_scripts': [
            'rscout = src.launcher:start',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop'
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)