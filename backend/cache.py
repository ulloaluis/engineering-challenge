# CACHE.PY

from collections import defaultdict
import config

"""
For the sake of this project, the cache is primarily used to
keep the data files in-memory. This prevents having to read
from disk each subsequent time we search for an item.

LRU (least recently used) cache, but essentially a wrapper
around a plain old dict. Could be much more efficient.

Note: no concurrency support
"""

class Cache:
    def __init__(self, limit=config.CACHE_LIMIT):
        # Limit specifies how many elements can be in the
        # cache before prompting eviction.
        self.cache = dict()
        self.metadata = defaultdict(int) # keeps track of accesses
        self.limit = limit

    def add(self, k, v):
        if k in self.cache:
            return
        if len(self.cache) == self.limit:
            self.evict()

        self.cache[k] = v

    def get(self, k):
        if k not in self.cache:
            return None

        self.metadata[k] += 1
        return self.cache[k]

    def evict(self):
        # Evict the entry which has been accessed the least.
        min_k = None
        for k in self.cache:
            if not min_k or self.metadata[k] < self.metadata[min_k]:
                min_k = k
        del self.cache[min_k]
        del self.metadata[min_k]

if __name__ == '__main__':
    print('WARNING: Running cache.py.')

    # TESTING
    cache = Cache(1)
    cache.add('dog', 1)
    assert cache.get('dog') == 1
    cache.add('cat', 2)
    assert not cache.get('dog')  # should've been evicted
    assert cache.get('cat') == 2

    cache = Cache(3)
    cache.add('a', 1)
    cache.add('b', 2)
    cache.add('c', 3)
    cache.get('a')
    cache.get('a')
    cache.get('b')
    cache.get('b')
    cache.add('d', 4)
    # Ensure least recently used (c) was evicted.
    assert not cache.get('c')
    assert cache.get('a') == 1
    assert cache.get('b') == 2
    assert cache.get('d') == 4

