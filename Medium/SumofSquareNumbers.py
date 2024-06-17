class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_num = int(math.sqrt(c))
        if sqrt_num * sqrt_num == c:
            return True
        max = round(sqrt_num)
        squares = [pow(i, 2) for i in range(1, max + 1)]
        left = 0
        right = len(squares) - 1
        while left <= right:
            if squares[left] + squares[right] < c:
                left += 1
            elif squares[left] + squares[right] > c:
                right -= 1
            else:
                return True
        return False
