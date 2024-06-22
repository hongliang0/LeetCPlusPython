class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlaceBalls(min_dist: int) -> bool:
            # Place the first ball in the first basket
            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    # Place another ball
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        # Sort the basket positions
        position.sort()

        # Binary search for the maximum minimum distance
        left, right = 1, position[-1] - position[0]
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
