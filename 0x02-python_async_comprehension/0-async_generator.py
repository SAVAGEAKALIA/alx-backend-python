#!/usr/bin/env python3
"""Task 0:  Async Generator"""

from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Function that loops 10 times to yield random numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
