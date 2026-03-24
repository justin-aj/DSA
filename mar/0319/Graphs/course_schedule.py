# Course Schedule - Cycle Detection
# Pattern: DFS + Two Sets (visited, cycle)
# Difficulty: Medium

def canFinish(n, prerequisites):
    graph = {i: [] for i in range(n)}
    for a, b in prerequisites:
        graph[a].append(b)

    visited, cycle = set(), set()

    def dfs(node):
        if node in cycle: return False   # cycle detected
        if node in visited: return True  # already processed safely

        cycle.add(node)        # entering node
        for n in graph[node]:
            if not dfs(n): return False
        cycle.remove(node)     # leaving node (backtrack)
        visited.add(node)      # fully processed
        return True

    for i in range(n):
        if not dfs(i): return False
    return True
