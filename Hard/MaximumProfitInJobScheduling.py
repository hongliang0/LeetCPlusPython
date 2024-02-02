class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            include_profit = jobs[i - 1][2]
            l = self.binarySearch(jobs, i - 1)
            if l != -1:
                include_profit += dp[l + 1]
            dp[i] = max(include_profit, dp[i - 1])
        return dp[n]

    def binarySearch(self, jobs, index):
        low, high = 0, index - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[index][0]:
                if mid == len(jobs) - 1 or jobs[mid + 1][1] > jobs[index][0]:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1
        return -1
