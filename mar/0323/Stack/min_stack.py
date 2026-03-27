# Min Stack
# Pattern: Two Stacks (stack + minstack)
# Difficulty: Medium

from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Time: O(1) for all operations
# Space: O(n)
# Key: minstack tracks minimum at every level
