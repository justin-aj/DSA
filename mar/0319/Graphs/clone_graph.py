# Clone Graph
# Pattern: DFS + Hashmap
# Difficulty: Medium

def cloneGraph(node):
    cloned = {}

    def dfs(node):
        if node in cloned: return cloned[node]
        clone = Node(node.val)
        cloned[node] = clone  # save BEFORE recursing to handle cycles
        for n in node.neighbors:
            clone.neighbors.append(dfs(n))
        return clone

    return dfs(node)
