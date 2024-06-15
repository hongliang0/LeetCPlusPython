class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums = {}
        for num in arr1:
            if num not in nums:
                nums[num] = 0
            nums[num] += 1
        new_arr = []
        for i in arr2:
            for _ in range(nums[i]):
                new_arr.append(i)
            del nums[i]
        for i in sorted(nums):
            for _ in range(nums[i]):
                new_arr.append(i)
        return new_arr
