#!/usr/bin/env python3
"""Task 2: Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine Function that measures time in parallel"""
    begin = time.perf_counter()
    results = \
        await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter() - begin
    return end
