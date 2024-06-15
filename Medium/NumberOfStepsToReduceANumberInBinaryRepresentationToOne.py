class Solution:
    def numSteps(self, s: str) -> int:
        int_s = int(s, 2)
        count = 0
        while int_s > 1:
            if int_s % 2 != 0:
                int_s += 1
                count += 1
            else:
                int_s //= 2
                count += 1
        return count
