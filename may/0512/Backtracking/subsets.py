# Subsets
# Pattern: Backtracking (Take or Skip)
# Difficulty: Medium
# LeetCode: 78

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, current):
            if i == len(nums):
                res.append(current[:])
                return

            # take nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)

            # skip nums[i]
            current.pop()
            backtrack(i + 1, current)

        backtrack(0, [])
        return res

# Trace for nums = [1, 2, 3]:
#
# backtrack(0, [])
# ├── take 1 → backtrack(1, [1])
# │   ├── take 2 → backtrack(2, [1,2])
# │   │   ├── take 3 → backtrack(3, [1,2,3]) → save [1,2,3]
# │   │   └── skip 3 → backtrack(3, [1,2]) → save [1,2]
# │   └── skip 2 → backtrack(2, [1])
# │       ├── take 3 → backtrack(3, [1,3]) → save [1,3]
# │       └── skip 3 → backtrack(3, [1]) → save [1]
# └── skip 1 → backtrack(1, [])
#     ├── take 2 → backtrack(2, [2])
#     │   ├── take 3 → backtrack(3, [2,3]) → save [2,3]
#     │   └── skip 3 → backtrack(3, [2]) → save [2]
#     └── skip 2 → backtrack(2, [])
#         ├── take 3 → backtrack(3, [3]) → save [3]
#         └── skip 3 → backtrack(3, []) → save []
#
# Result: [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]
# Key: current.pop() undoes the "take" before trying "skip" — that's the "back" in backtracking
