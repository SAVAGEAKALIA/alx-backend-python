#!/usr/bin/env python3
""" Task 1: execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously function to spawn wait_random n times"""
    async_list = []
    for i in range(n):
        delay = await asyncio.gather(wait_random(max_delay))
        async_list.extend(delay)

    for m in range(len(async_list)):
        for n in range(m + 1, len(async_list)):
            if async_list[m] > async_list[n]:
                async_list[m], async_list[n] = async_list[n], async_list[m]
                # print(f"Swapped {async_list[m]} and {async_list[n]}")
    return async_list
