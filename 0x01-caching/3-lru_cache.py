#!/usr/bin/env python3
"""Task 3.LRU Caching"""

from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    """
    LRUCache implements Least Recently Used replacement policy
    """

    def __init__(self):
        super().__init__()
        self.lru_list = []

    def put(self, key: str, item: str) -> None:
        """assigns a key value in the cache dictionary"""
        if key is None or item is None:
            return
        cache_len = len(self.cache_data)
        max_i = super().MAX_ITEMS

        if cache_len >= max_i and key not in self.cache_data:
            discarded = self.lru_list[0]
            if discarded in self.cache_data:
                del self.cache_data[discarded]
            self.lru_list.remove(discarded)
            print(f"DISCARD: {discarded}")

        self.cache_data[key] = item
        if key in self.lru_list:
            self.lru_list.remove(key)
        self.lru_list.append(key)
        # print('lru_list: ', self.lru_list)

    def get(self, key: str) -> Any:
        """Fetch key data from cache"""
        if key in self.lru_list:
            self.lru_list.remove(key)
            self.lru_list.append(key)
        # print('lru_list: ', self.lru_list)
        return self.cache_data.get(key, None)
