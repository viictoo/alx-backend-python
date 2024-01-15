#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): int arguments (in this order): n
        max_delay (int): integer argument
    Returns:
        List[float]:  total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish = time.time()
    return (finish - start) / n


if __name__ == '__main__':
    """caller"""
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
