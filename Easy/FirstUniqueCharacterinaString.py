class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordbank = {}
        for index in range(len(s)):
            if s[index] not in wordbank:
                wordbank[s[index]] = index
            else:
                wordbank[s[index]] = -1
        wordbank = dict(sorted(wordbank.items(), key=lambda x: x[1]))
        for item in wordbank:
            if wordbank[item] != -1:
                return wordbank[item]
        return -1
