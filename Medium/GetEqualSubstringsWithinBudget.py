class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ascii_arr = []
        left, right, curr_sum, max_len = 0, 0, 0, 0

        for i in range(len(s)):
            ascii_arr.append(abs(ord(s[i]) - ord(t[i])))

        while right < len(s):
            curr_sum += ascii_arr[right]
            while curr_sum > maxCost:
                curr_sum -= ascii_arr[left]
                left += 1
            max_len = max(max_len, right - left + 1)
            print(f"left at {left} right at {right} len is {right - left}")
            right += 1
        return max_len
