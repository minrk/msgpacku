#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Min RK.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function

import os
import sys

from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version
version_ns = {}
with open(pjoin(here, 'msgpacku.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, {}, version_ns)


setup_args = dict(
    name                = 'msgpacku',
    version             = version_ns['__version__'],
    py_modules          = ['msgpacku'],
    description         = "Unicode-friendly wrapper around msgpack.",
    long_description    = """A tiny wrapper around msgpack to use bin_type and text encoding by default.""",
    author              = "Min RK",
    author_email        = "benjaminrk@gmail.com",
    url                 = "https://github.com/minrk/msgpacku",
    license             = "BSD",
    install_requires    = [
        'msgpack-python',
    ],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

if 'bdist_wheel' in sys.argv:
    import setuptools


if __name__ == '__main__':
    setup(**setup_args)
