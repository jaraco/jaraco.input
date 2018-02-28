#!/usr/bin/env python

"""
Input support
"""

# $Id$

__all__ = ['Joystick']

import sys

platform_path = '.'.join((__name__, sys.platform))

try:
	mod = __import__(platform_path, globals(), locals(), ['Joystick'])
	Joystick = mod.Joystick
except ImportError:
	pass
