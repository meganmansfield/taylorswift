#!/usr/bin/env python  
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import os
import sys
from setuptools import setup

sys.path.insert(0, "taylorswift")
from version import __version__


long_description = \
    """
taylorswift is a python package that will find you the perfect Taylor Swift song
to match your mood.

"""


setup(name='taylorswift',
      version=__version__,
      description='Find the perfect Taylor Swift song to match your mood',
      packages=['taylorswift'],
      install_requires=['numpy'],
      author='Megan Mansfield',
      author_email='meganmansfield@uchicago.edu',
      license='MIT',
      long_description = long_description,
      url='https://github.com/meganmansfield/taylorswift',
      package_data={'': ['README.md', 'LICENSE']},
      include_package_data=True,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.0',
        ],
      )
