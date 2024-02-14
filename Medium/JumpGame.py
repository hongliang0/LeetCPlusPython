class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Define two pointers, current location and max jumpable location
        max_location = nums[0]
        for i in range(len(nums)):
            if max_location >= i:
                max_location = max(max_location, nums[i] + i)
            else:
                return False
        return max_location >= len(nums) - 1
