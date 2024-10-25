#!/usr/bin/env python3
""" Function Task: Type Checking """
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms a given array by a given factor.

    Args:
        lst (Tuple[int,...]): The input array.
        :param lst:
        :param factor: """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
