#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay

    Args:
        n (int): int arguments (in this order): n
        max_delay (int): integer argument
    Returns:
        List[float]:  list of all the delays (float values).
        The list of the delays should be in ascending order without
        using sort() because of concurrency
    """

    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]


if __name__ == '__main__':
    """caller"""
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
