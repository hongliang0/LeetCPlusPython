class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                max_val = grid[i - 1][j - 1]
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        max_val = max(max_val, grid[i + di][j + dj])
                maxLocal[i - 1][j - 1] = max_val

        return maxLocal
