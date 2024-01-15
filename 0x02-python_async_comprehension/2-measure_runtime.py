#!/usr/bin/env python3
"""Measure runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes comprehension 4 times in parallel and Measure runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    fin = time.perf_counter()
    return fin - start
