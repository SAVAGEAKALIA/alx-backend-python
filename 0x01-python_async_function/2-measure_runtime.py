#!/usr/bin/env python3
"""Task 2: Async Task to Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the time taken for n coroutines to complete,
    with each coroutine having a random delay up to max_delay seconds.
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_diff = time.perf_counter() - s
    total = time_diff / n
    return total
