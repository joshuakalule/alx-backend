#!/usr/bin/env python3
"""Task 1. FIFO caching"""

from base_caching import BaseCaching
from typing import Any


class FIFOCache(BaseCaching):
    """
    FIFOCache implements caching with the FIFO policy
    """

    def __init__(self):
        super().__init__()
        self.fifo_key_list = []

    def put(self, key: str, item: str) -> None:
        """assigns a key value in the cache dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            pass
        elif len(self.cache_data) >= super().MAX_ITEMS:
            discarded = self.fifo_key_list.pop(0)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        self.cache_data[key] = item
        self.fifo_key_list.append(key)

    def get(self, key: str) -> Any:
        """Fetch key data from cache"""
        return self.cache_data.get(key, None)
