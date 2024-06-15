class Solution:
    def longestPalindrome(self, s: str) -> str:
        my_dict = {}
        summer = 0
        forever_single = True
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 0
            my_dict[s[i]] += 1
        for word in my_dict:
            if my_dict[word] % 2 == 0:
                summer += my_dict[word]
            elif forever_single:
                forever_single = False
                summer += my_dict[word]
            else:
                summer += my_dict[word] - 1
        return summer
