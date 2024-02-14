class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialise dynamic programming array
        n = len(nums)
        dp = [n] * n

        # Base Case
        dp[0] = 0

        # Begin populating array
        for i in range(n):
            for j in range(i, min(n - 1, i + nums[i]) + 1):
                dp[j] = min(1 + dp[i], dp[j])
        # print(dp)
        return dp[-1]
