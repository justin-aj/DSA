# Max Subarray Sum of Size K
# Pattern: Sliding Window
# Difficulty: Easy

def maxSubarraySum(nums, k):
    window_sum = sum(nums[0:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
