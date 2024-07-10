#!/usr/bin/env python3
import asyncio
from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehending over async_generator, then return the 10 random numbers."""
    return [i async for i in async_generator()]

