# Product of Array Except Self
# Pattern: Prefix + Suffix Products
# Difficulty: Medium

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        
        return out

# Time: O(n)
# Space: O(1) — output array doesn't count as extra space
# Key insight: out[i] = product of all LEFT * product of all RIGHT
