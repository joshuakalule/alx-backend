#!/usr/bin/env python3
"""
Task 0. Simple helper function
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index for range of indexes to return in a list"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
