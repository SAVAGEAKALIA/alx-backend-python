#!/usr/bin/env python3
"""Task 4: Async Task Recall"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function task_wait_n for n times
    Call task_wait_random
    """
    async_list = []
    for i in range(n):
        delay = await asyncio.gather(task_wait_random(max_delay))
        async_list.extend(delay)

    for m in range(len(async_list)):
        for n in range(m + 1, len(async_list)):
            if async_list[m] > async_list[n]:
                async_list[m], async_list[n] = async_list[n], async_list[m]
                # print(f"Swapped {async_list[m]} and {async_list[n]}")
    return async_list
