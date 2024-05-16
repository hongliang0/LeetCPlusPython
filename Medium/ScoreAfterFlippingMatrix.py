class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        hori = len(grid[0])
        verti = len(grid)

        for i in range(verti):
            if grid[i][0] == 0:
                for j in range(hori):
                    grid[i][j] = 1 - grid[i][j]
        for i in range(hori):
            col_sum = sum(grid[j][i] for j in range(verti))
            if col_sum < verti / 2:
                for j in range(verti):
                    grid[j][i] = 1 - grid[j][i]

        total_sum = 0
        for i in range(verti):
            for j in range(hori):
                total_sum += grid[i][j] * pow(2, hori - j - 1)
        return total_sum
