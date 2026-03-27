# Top K Frequent Elements - Heap Solution
# Pattern: Min Heap of size k
# Difficulty: Medium

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # order by freq!
            if len(heap) > k:
                heapq.heappop(heap)  # remove least frequent

        return [num for freq, num in heap]

# Time: O(n log k)
# Space: O(n)
# Key: store (freq, num) so heap orders by frequency
# heappop removes LEAST frequent → only top k remain
