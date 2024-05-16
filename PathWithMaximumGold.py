class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(curr_x, curr_y):

            # Check boundary
            if curr_x < 0 or curr_x >= len(grid) or curr_y < 0 or curr_y >= len(grid[0]) or grid[curr_x][curr_y] == 0:
                return 0

            # Set curr_loc to 0
            original_gold = grid[curr_x][curr_y]
            grid[curr_x][curr_y] = 0

            # dfs, NOT DP
            gold_collected = max(
                dfs(curr_x - 1, curr_y),
                dfs(curr_x + 1, curr_y),
                dfs(curr_x, curr_y - 1),
                dfs(curr_x, curr_y + 1)
            ) + original_gold

            # Reset location for alternative path
            grid[curr_x][curr_y] = original_gold
            return gold_collected

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    # Check eachs start from each start
                    max_gold = max(max_gold, dfs(i, j))

        return max_gold
