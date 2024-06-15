class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iterator = 1
        while iterator < len(nums):
            pointer = iterator
            while pointer > 0 and nums[pointer] < nums[pointer - 1]:
                temp = nums[pointer]
                nums[pointer] = nums[pointer - 1]
                nums[pointer - 1] = temp
                pointer = pointer - 1
            iterator += 1
        return
