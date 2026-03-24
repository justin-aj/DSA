# Subtree of Another Tree
# Pattern: DFS + Same Tree
# Difficulty: Easy

def isSubtree(root, sub):
    if root is None: return False
    if root.val == sub.val and isSameTree(root, sub): return True
    return isSubtree(root.left, sub) or isSubtree(root.right, sub)

def isSameTree(p, q):
    if not p and not q: return True
    if not p or not q: return False
    if p.val != q.val: return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
