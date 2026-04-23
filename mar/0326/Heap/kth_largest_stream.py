# Kth Largest Element in a Stream
# Pattern: Min Heap of size k
# Difficulty: Easy

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        self.nums = nums

        for num in self.nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)  # remove smallest, keep top k
        return self.hp[0]  # kth largest = top of min heap

# Time: O(n log k) for init, O(log k) for each add
# Space: O(k)
# Key: min heap of size k → top is always kth largest
