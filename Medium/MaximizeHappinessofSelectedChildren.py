class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happykids = 0
        for i in range(k):
            happykids += max(0, happiness[i] - i)
        return happykids
