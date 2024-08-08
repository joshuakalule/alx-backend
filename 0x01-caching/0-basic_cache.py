#!/usr/bin/env python3
"""Task 0. Basic Dictionary"""

from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """
    Basic Cache implements put and get methods
    """

    def put(self, key: str, item: str) -> None:
        """assigns a key value to the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """Fetch key data from cache"""
        return self.cache_data.get(key, None)
