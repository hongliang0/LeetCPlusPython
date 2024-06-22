class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        def atMostTarget(target):
            left, total, found = 0, 0, 0
            for right, val in enumerate(nums):
                total += val
                while total > target and left <= right:
                    total -= nums[left]
                    left += 1
                found += right - left + 1
            return found

        return atMostTarget(k) - atMostTarget(k - 1)
