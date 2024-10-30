#!/usr/bin/env python3
"""Task 1: Async Comprehensions"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine function to use async comprehension list"""
    results = [random_num async for random_num in async_generator()]
    return results
