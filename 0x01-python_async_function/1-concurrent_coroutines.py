#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Asynchronously function to spawn wait_random n times"""
    async_list = []
    for i in range(n):
        delay = await asyncio.gather(wait_random(max_delay))
        async_list.extend(delay)
        # delay = wait_random(max_delay)
        # async_list.append(max_delay)
        # for m in range(len(async_list)):
        #     for n in range(m+1, len(async_list)):
        #         if async_list[m] > async_list[n]:
        #             async_list[m], async_list[n] = async_list[n], async_list[m]
        #             print(f"Swapped {async_list[m]} and {async_list[n]}")
    # delay = await asyncio.gather(wait_random(async_list[0:2]))
    for m in range(len(async_list)):
        for n in range(m + 1, len(async_list)):
            if async_list[m] > async_list[n]:
                async_list[m], async_list[n] = async_list[n], async_list[m]
                # print(f"Swapped {async_list[m]} and {async_list[n]}")
    return async_list
