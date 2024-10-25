#!/usr/bin/env python3
"""Function tasks for complex types annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key-value pair into a tuple"""
    return k, v ** 2
