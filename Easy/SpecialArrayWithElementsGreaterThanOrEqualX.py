# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         for i in range(1, len(nums) + 1):
#             i_counter = 0
#             for j in range(len(nums)):
#                 if nums[j] >= i:
#                     i_counter += 1
#             if i_counter == i and i_counter != 0:
#                 return i_counter
#         return -1

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort nums in descending order
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= i and (i == len(nums) or nums[i] < i):
                return i
        return -1
