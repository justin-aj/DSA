class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        j = 0
        for element in list(set(nums)):
            val = element - 1
            if val not in nums:
                l = 0
                while element + l in nums:
                    l = l + 1
                j = max(l, j)
        return j
