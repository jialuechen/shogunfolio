"""
The :mod:`shogunfolio.exceptions` module includes all custom warnings and error
classes used across shogunfolio.
"""

# Copyright (c) 2023
# Author: Hugo Delatte <jialuechen@outlook.com>
# License: BSD 3 clause

__all__ = [
    "OptimizationError",
    "EquationToMatrixError",
    "GroupNotFoundError",
    "NonPositiveVarianceError",
]


class OptimizationError(Exception):
    """Optimization Did not converge"""


class EquationToMatrixError(Exception):
    """Error while processing equations"""


class GroupNotFoundError(Exception):
    """Group name not found in the groups"""


class NonPositiveVarianceError(Exception):
    """Variance negative or null"""
