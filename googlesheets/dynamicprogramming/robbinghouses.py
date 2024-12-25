class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            print(num + rob1, rob2)
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            print(rob1, rob2)
        return rob2
