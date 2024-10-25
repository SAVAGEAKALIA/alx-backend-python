#!/usr/bin/env python3
""" Function Task that take a list of float to return sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of all elements in the input list using a generator expression.

    Args:
        input_list (list[float]): List of numbers to be summed.

    Returns:
        float: Sum of all elements in the input list.
    """
    return sum(input_list)
