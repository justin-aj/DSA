class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = list(set(nums))
        print(n)
        if n == nums:
            return False
        else:
            return True