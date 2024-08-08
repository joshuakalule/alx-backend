#!/usr/bin/env python3
"""Task 4. MRU Caching"""

from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """
    MRUCache implements Most Recently Used policy
    """

    def __init__(self):
        super().__init__()
        self.mru_list = []

    def put(self, key: str, item: str) -> None:
        """assigns a key value in the cache dictionary"""
        if key is None or item is None:
            return
        cache_len = len(self.cache_data)
        max_i = super().MAX_ITEMS

        if cache_len >= max_i and key not in self.cache_data:
            discarded = self.mru_list[max_i - 1]
            if discarded in self.cache_data:
                del self.cache_data[discarded]
            self.mru_list.remove(discarded)
            print(f"DISCARD: {discarded}")

        self.cache_data[key] = item
        if key in self.mru_list:
            self.mru_list.remove(key)
        self.mru_list.append(key)
        # print('mru_list: ', self.mru_list)

    def get(self, key: str) -> Any:
        """Fetch key data from cache"""
        if key in self.mru_list:
            self.mru_list.remove(key)
            self.mru_list.append(key)
        # print('mru_list: ', self.mru_list)
        return self.cache_data.get(key, None)
