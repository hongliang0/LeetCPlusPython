class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostTarget(target):
            left, total, found = 0, 0, 0
            for right, val in enumerate(nums):
                total += val
                while total > target and left <= right:
                    total -= nums[left]
                    left += 1
                found += right - left + 1
            return found

        return atMostTarget(goal) - atMostTarget(goal - 1)
