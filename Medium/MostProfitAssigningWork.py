class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(profit, difficulty), reverse=True)
        money = 0
        for work in worker:
            for i in range(len(jobs)):
                if work >= jobs[i][1]:
                    money += jobs[i][0]
                    break
        return money
