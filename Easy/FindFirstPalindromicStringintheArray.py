class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            is_palindrome = True
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - i - 1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return word
        return ""
