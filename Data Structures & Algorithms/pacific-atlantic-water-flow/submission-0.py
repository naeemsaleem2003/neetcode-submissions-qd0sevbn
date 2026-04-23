class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        atl = [[False] * cols for _ in range(rows)]
        pac = [[False] * cols for _ in range(rows)]
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
        for c in range(cols):
            dfs(0, c, pac, float('-inf'))
        for r in range(rows):
            dfs(r, 0, pac, float('-inf'))
        for c in range(cols):
            dfs(rows - 1, c, atl, float('-inf'))
        for r in range(rows):
            dfs(r, cols - 1, atl, float('-inf'))
        ans = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    ans.append([r, c])
        return ans
