#!/usr/bin/env python2.4
"""
setup.py - script for building MyApplication

Usage:
    % python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    app=['main.py'],
)
