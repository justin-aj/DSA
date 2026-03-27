# Daily Temperatures
# Pattern: Monotonic Stack
# Difficulty: Medium

from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx  # days difference
            stack.append(i)

        return result

# Time: O(n)
# Space: O(n)
# Key: Monotonic Stack — stores indices of days waiting for warmer temp
# When warmer day found → pop and calculate difference
