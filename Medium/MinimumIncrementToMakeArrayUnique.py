class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        last_insertion = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= last_insertion:
                counter += last_insertion - nums[i] + 1
                last_insertion += 1
            else:
                last_insertion = nums[i]
        return counter
