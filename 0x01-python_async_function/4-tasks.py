#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay

    Args:
        n (int): int arguments (in this order): n
        max_delay (int): integer argument
    Returns:
        List[float]:  list of all the delays (float values).
        The list of the delays should be in ascending order without
        using sort() because of concurrency
    """

    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]


if __name__ == '__main__':
    """caller"""
    task_wait_n = __import__('4-tasks').task_wait_n

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
