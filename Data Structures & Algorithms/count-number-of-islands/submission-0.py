class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    island += 1
                    queue.append((r, c))
                    seen.add((r, c))

                    while queue:

                        ro, co = queue.popleft()

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = ro + dr, co + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                                queue.append((nr, nc))
                                seen.add((nr, nc))
        
        return island
            



