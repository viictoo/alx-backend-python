#!/usr/bin/env python3
"""asyc module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    return random.uniform(0, max_delay)


if __name__ == '__main__':
    import asyncio
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
