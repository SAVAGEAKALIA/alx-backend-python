#!/usr/bin/env python3
# # countasync.py
#
# import asyncio
#
# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    # Create a task to run say_hello concurrently
    task = asyncio.create_task(say_hello())

    # Do other things while say_hello runs in the background
    await asyncio.sleep(0.5)
    print("Meanwhile...")

    # Await the task to ensure it completes
    await task


# Run the main function
asyncio.run(main())
