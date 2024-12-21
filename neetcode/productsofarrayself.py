class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize the output array with 1s

        # Calculate prefix product for each element
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]

        # Calculate suffix product and multiply it with the prefix product
        suffix = 1
        for i in range(n - 1, -1, -1):  # Traverse from the end
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]

        return output
