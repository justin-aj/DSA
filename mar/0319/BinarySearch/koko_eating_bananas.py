# Koko Eating Bananas
# Pattern: Binary Search on Answer Space
# Difficulty: Medium

from math import ceil

def minEatingSpeed(piles, h):
    def canFinish(k):
        return sum(ceil(p / k) for p in piles) <= h

    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2
        if canFinish(mid): right = mid - 1  # try slower
        else: left = mid + 1                # too slow, go faster
    return left
