#!/usr/bin/env python3
"""Function Task for mix annotated functions"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all numbers in a mixed list"""
    return sum(mxd_lst)
