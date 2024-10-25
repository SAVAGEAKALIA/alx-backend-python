#!/usr/bin/env python3
"""Task 3: Import  and use previous Async Calls"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task function to await wait_random"""
    delay = asyncio.create_task(wait_random(max_delay))
    return delay
