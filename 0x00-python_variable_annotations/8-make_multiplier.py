#!/usr/bin/env python3
"""Function Tasks Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by a given multiplier."""
    return lambda x: x * multiplier
