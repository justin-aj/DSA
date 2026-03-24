# Validate Binary Search Tree
# Pattern: BFS + Min/Max Range
# Difficulty: Medium

from collections import deque

def isValidBST(root):
    queue = deque([(root, float('-inf'), float('inf'))])
    while queue:
        node, min_val, max_val = queue.popleft()
        if node is None: continue
        if node.val <= min_val or node.val >= max_val: return False
        queue.append((node.left, min_val, node.val))
        queue.append((node.right, node.val, max_val))
    return True
