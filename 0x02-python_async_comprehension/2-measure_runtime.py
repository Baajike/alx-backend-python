#!/usr/bin/env python3
import asyncio
import time
from typing import List
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure the total runtime."""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time

