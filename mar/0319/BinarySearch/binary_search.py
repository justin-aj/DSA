# Classic Binary Search
# Pattern: Binary Search
# Difficulty: Easy

def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        elif nums[mid] > target: right = mid - 1
        else: left = mid + 1
    return -1
