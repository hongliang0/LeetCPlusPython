class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1
        ans = [key for key, value in my_dict.items() if value == 1]
        return ans
