class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        a = set({0})

        t = sum(nums) // 2
        for i in range(len(nums)):
            nexta = a.copy()
            for j in a:
                total = j + nums[i]
                nexta.add(total)
            a = nexta

        return True if t in a else False