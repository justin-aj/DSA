# Hand of Straights
# Pattern: Greedy + Min Heap + Hashmap
# Difficulty: Medium
# LeetCode: 846

from collections import Counter
import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hashmap = Counter(hand)
        heap = list(hashmap.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if not hashmap[i]:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    if heap[0] != i:
                        return False
                    heapq.heappop(heap)

        return True
