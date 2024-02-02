class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if s[i] == 'C' and i < len(s) - 1 and s[i + 1] == 'M':
                total += 900
                i += 2
            elif s[i] == 'C' and i < len(s) - 1 and s[i + 1] == 'D':
                total += 400
                i += 2
            elif s[i] == 'X' and i < len(s) - 1 and s[i + 1] == 'L':
                total += 40
                i += 2
            elif s[i] == 'X' and i < len(s) - 1 and s[i + 1] == 'C':
                total += 90
                i += 2
            elif s[i] == 'I' and i < len(s) - 1 and s[i + 1] == 'V':
                total += 4
                i += 2
            elif s[i] == 'I' and i < len(s) - 1 and s[i + 1] == 'X':
                total += 9
                i += 2
            elif s[i] == 'M':
                total += 1000
                i += 1
            elif s[i] == 'D':
                total += 500
                i += 1
            elif s[i] == 'C':
                total += 100
                i += 1
            elif s[i] == 'L':
                total += 50
                i += 1
            elif s[i] == 'X':
                total += 10
                i += 1
            elif s[i] == 'V':
                total += 5
                i += 1
            elif s[i] == 'I':
                total += 1
                i += 1
        return total
