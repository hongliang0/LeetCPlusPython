class Solution:
    def numSquares(self, n: int) -> int:
        # Find all square numbers smaller or equal to target
        squares = []
        count = 1
        while pow(count, 2) <= n:
            squares.append(pow(count, 2))
            count += 1

        # Utilise dynamic programming to reach optimal conclusion
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        # Use dynamic programming to iterate backwards
        for i in range(1, n + 1):
            for j in squares:
                if i >= j:
                    dp[i] = min(dp[i - j] + 1, dp[i])
                # print(f"At {i} we have {dp[i]}")
        # Return solution
        return dp[-1]
