"""
Input support
"""

__all__ = ['Joystick']

import importlib
import sys

platform_path = '.'.join((__name__, sys.platform))

try:
    Joystick = importlib.import_module(platform_path).Joystick
except ImportError:
    pass
