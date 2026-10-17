"""
Input support
"""

__all__ = ['Joystick']

import importlib
import sys

platform_path = f'{__name__}.{sys.platform}'

try:
    Joystick = importlib.import_module(platform_path).Joystick  # type: ignore
except ImportError:
    pass
