# Valid Parentheses
# Pattern: Stack
# Difficulty: Easy

from collections import deque
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {")": "(", "}": "{", "]": "["}
        stack = deque()

        for c in s:
            if c in bracket:
                if stack and stack[-1] == bracket[c]:
                    stack.pop()
                else:
                    return False  # no matching opening bracket
            else:
                stack.append(c)

        return not stack  # stack should be empty if valid

# Time: O(n)
# Space: O(n)
# Key: map closing → opening bracket, use stack to track opens
