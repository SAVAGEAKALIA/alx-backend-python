#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay=10):
    """ Basic async function code"""
    delay = random.uniform(0, max_delay)
    # print(f"Waiting random time...{delay:0.2f}")
    await asyncio.sleep(delay)
    return delay
