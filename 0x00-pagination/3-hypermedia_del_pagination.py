#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Return deletion-resilient response."""
        indexed_dataset = self.indexed_dataset()
        if index:
            assert index > 0 and index < len(indexed_dataset)

        idx = -1 if index is None else index
        pages = page_size
        data = []
        if len(indexed_dataset) > 0:
            while pages > 0:
                if idx in indexed_dataset:
                    data.append(indexed_dataset[idx])
                    pages -= 1
                idx += 1

        if len(data) > 0:
            next_index = None if idx not in indexed_dataset else idx
        else:
            next_index = None

        _page_size = len(data)

        return {
            'index': index,
            'data': data,
            'page_size': _page_size,
            'next_index': next_index
        }
