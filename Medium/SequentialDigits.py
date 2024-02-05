class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        # Determine the minimum and maximum number of digits
        min_digits = len(str(low))
        max_digits = len(str(high))

        # Generate all possible digits
        # Start with generating the lengths of possible digits
        for length in range(min_digits, max_digits + 1):
            # Start with generating the start of the sequential digits
            for starting_digit in range(1, 10):
                num = 0
                tracking_num = starting_digit
                for i in range(length):
                    num = num * 10 + tracking_num
                    if tracking_num == 9:
                        break
                    else:
                        tracking_num += 1

                if low <= num <= high:
                    result.append(num)

        return sorted(set(result))
