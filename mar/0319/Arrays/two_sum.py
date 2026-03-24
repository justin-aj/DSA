# Two Sum
# Pattern: Hashmap
# Difficulty: Easy

def twoSum(nums, target):
    maps = {}
    for num in nums:
        if num in maps:
            return [num, maps[num]]
        maps[target - num] = num
