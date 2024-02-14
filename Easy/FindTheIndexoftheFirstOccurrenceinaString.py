class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_pointer = 0
        ne_pointer = 0
        # While needle pointer has not reached the end
        while ne_pointer < len(needle) and hay_pointer < len(haystack):
            # If the words don't align
            if haystack[hay_pointer] != needle[ne_pointer]:
                # print(f"Words don't align {haystack[hay_pointer]} and {needle[ne_pointer]}")
                hay_pointer -= ne_pointer - 1
                ne_pointer = 0
            else:
                hay_pointer += 1
                ne_pointer += 1
            # If the words align
            if len(needle) == ne_pointer:
                # print(f"FOUND")
                return hay_pointer - ne_pointer
        return -1
