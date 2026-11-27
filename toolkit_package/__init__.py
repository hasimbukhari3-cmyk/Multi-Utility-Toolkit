"""
toolkit_package - Custom package for Multi-Utility Toolkit.

This package contains modules for file operations and mathematical utilities.

Modules:
    file_operations: Functions for reading, writing, and managing files.
    math_utilities: Functions for advanced mathematical calculations and conversions.
"""

from . import file_operations
from . import math_utilities

__all__ = ['file_operations', 'math_utilities']
__version__ = '1.0.0'
