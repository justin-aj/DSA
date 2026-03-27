# Car Fleet
# Pattern: Monotonic Stack
# Difficulty: Medium

from collections import deque
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = deque()

        for pos, speed in pairs:
            time = (target - pos) / speed
            # if current time > stack top → slower car → new fleet → push
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

# Time: O(n log n) — sorting
# Space: O(n)
# Key: sort by position descending (closest to target first)
# SLOWER (time > top)  → new fleet  → PUSH
# FASTER (time <= top) → catches up → SKIP
