# Longest Consecutive Sequence
# Pattern: HashSet
# Difficulty: Medium
# Key fix: convert nums to set for O(1) lookup!

def longestConsecutive(nums):
    nums = set(nums)  # O(1) lookup instead of O(n) on list!
    max_len = 0

    for num in nums:
        if num - 1 not in nums:  # only start from sequence beginning
            length = 1
            while num + 1 in nums:
                num += 1
                length += 1
            max_len = max(max_len, length)

    return max_len

# Time: O(n) — each number visited at most twice
# Space: O(n) — for the set
