#!/usr/bin/env python3
"""
Task 2. Hypermedia pagination
"""

import csv
import math
from typing import List, Optional, Tuple, TypedDict


class PageType(TypedDict):
    """Custom type for response"""
    page_size: int
    page: int
    data: List[List]
    next_page: Optional[int]
    prev_page: Optional[int]
    total_pages: int


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end index for range of indexes to return in a list
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> PageType:
        """Returns a paginated response as a dict"""
        dataset = self.dataset()

        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(dataset)/page_size)

        _page_size = len(data)

        next_page = None if page + 1 >= total_pages else page + 1

        prev_page = None if page - 1 <=0 else page - 1

        return {
            'page_size': _page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns list as required py page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if dataset is None or start > len(dataset):
            return []
        return dataset[start:end]
