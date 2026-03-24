# Number of Islands
# Pattern: DFS on Grid
# Difficulty: Medium

def numIslands(grid):
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]): return
        if visited[r][c] or grid[r][c] == '0': return
        visited[r][c] = 1
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count
