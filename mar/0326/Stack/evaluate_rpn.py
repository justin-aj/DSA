# Evaluate Reverse Polish Notation
# Pattern: Stack
# Difficulty: Medium

from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for tok in tokens:
            if tok in operators:
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                if tok == "+": stack.append(a + b)
                elif tok == "-": stack.append(a - b)
                elif tok == "*": stack.append(a * b)
                elif tok == "/": stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(tok))

        return stack[0]

# Time: O(n)
# Space: O(n)
# Key: use int(a/b) NOT a//b for truncation toward zero
