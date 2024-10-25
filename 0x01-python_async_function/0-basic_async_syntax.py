#!/usr/bin/env python3
"""Task 0: The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Basic async function code
        :param: max_delay:
    """
    delay = random.uniform(0, max_delay)
    # print(f"Waiting random time...{delay:0.2f}")
    await asyncio.sleep(delay)
    return delay
