class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_copy = score.copy()
        score_copy.sort(reverse=True)
        mydict = {}
        for i in range(len(score_copy)):
            mydict[score_copy[i]] = i
        for i in range(len(score)):
            if mydict[score[i]] == 0:
                score[i] = "Gold Medal"
            elif mydict[score[i]] == 1:
                score[i] = "Silver Medal"
            elif mydict[score[i]] == 2:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(mydict[score[i]] + 1)
        return score
