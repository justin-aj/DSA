# Level Order Traversal (BFS)
# Pattern: BFS with level grouping
# Difficulty: Medium

from collections import deque

def levelOrder(root):
    queue = deque([root])
    result = []
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
