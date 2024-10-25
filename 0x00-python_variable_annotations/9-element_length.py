#!/usr/bin/env python3
"""Function Task to Annotate Iterable Objects """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples,
    where each tuple contains a sequence and its length."""
    return [(i, len(i)) for i in lst]
