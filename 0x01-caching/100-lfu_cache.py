#!/usr/bin/env python3
"""Task 5. LFU Caching"""

from base_caching import BaseCaching
from typing import Any


class LFUCache(BaseCaching):
    """
    LFUCache implements Least Frequenctly Used policy
    """

    def __init__(self):
        super().__init__()
        # (key, count), ...
        self.discard_list = []

    def put(self, key: str, item: str) -> None:
        """assigns a key value in the cache dictionary"""
        if key is None or item is None:
            return
        cache_len = len(self.cache_data)
        max_i = super().MAX_ITEMS

        if cache_len >= max_i and key not in self.cache_data:
            discarded = self.discard_list.pop(0)[0]
            if discarded in self.cache_data:
                del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

        self.cache_data[key] = item
        # lower priority of removing new key if exists
        for k, count in {p[0]: p[1] for p in self.discard_list}.items():
            if k == key:
                self.discard_list.remove((k, count))
        # place new key before all available keys with lower priorities
        idx = -1
        for i in range(len(self.discard_list) - 1, -1, -1):
            count = self.discard_list[i][1]
            if count == 0:
                idx = i
                break
        if idx == -1:
            self.discard_list.insert(0, (key, 0))
        elif idx >= len(self.discard_list) - 1:
            self.discard_list.append((key, 0))
        else:
            self.discard_list.insert(idx + 1, (key, 0))
        # print("(put)discard_list", self.discard_list)

    def get(self, key: str) -> Any:
        """Fetch key data from cache"""
        for k, count in {p[0]: p[1] for p in self.discard_list}.items():
            if k == key:
                self.discard_list.remove((k, count))
                self.discard_list.append((k, count + 1))
        # print("(get)discard_list", self.discard_list)
        return self.cache_data.get(key, None)
