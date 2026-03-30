# Trapping Rain Water
# Pattern: Two Pointers
# Difficulty: Hard

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        water = 0
        while left < right:
            if height[left] <= height[right]:
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]  # NOT min() — two pointer guarantees maxLeft is limiting wall
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]  # NOT min() — two pointer guarantees maxRight is limiting wall
                right -= 1
        return water

# Time: O(n)
# Space: O(1)
# Key: process shorter side first
# Left branch:  water += maxLeft - height[left]
# Right branch: water += maxRight - height[right]
# min() doesn't work with two pointers — maxRight starts at 0!
