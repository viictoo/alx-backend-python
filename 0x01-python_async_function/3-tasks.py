#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and returns a asyncio.Task

    Args:       max_delay (int): integer argument
    Returns:    asyncio.Task:  task
    """

    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    """caller"""

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
