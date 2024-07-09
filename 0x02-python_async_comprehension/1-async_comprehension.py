#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers."""
    return [x async for x in async_generator()]
