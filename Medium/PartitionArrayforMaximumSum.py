class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            max_val = 0
            for j in range(1, min(k, i + 1) + 1):
                max_val = max(max_val, arr[i - j + 1])
                if i >= j:
                    dp[i] = max(dp[i], dp[i - j] + max_val * j)
                else:
                    dp[i] = max(dp[i], max_val * j)

        return dp[-1]
