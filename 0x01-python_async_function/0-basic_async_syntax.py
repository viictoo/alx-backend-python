#!/usr/bin/env python3
"""asyc module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """ waits for a random delay between 0 and max_delay
    (included and float value)
        seconds and eventually returns it
    """
    return random.uniform(0, max_delay)
