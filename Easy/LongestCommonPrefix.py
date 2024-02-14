class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        n = len(strs)
        for i in range(1, n):
            # Look at the word
            length = min(len(strs[i]), len(longest_prefix))
            new_prefix = []
            for char in range(length):
                if longest_prefix[char] == strs[i][char]:
                    new_prefix.append(longest_prefix[char])
                    # print(f"Matching prefix found: {longest_prefix[char]}")
                else:
                    break
            longest_prefix = ''.join(new_prefix)
        return longest_prefix
