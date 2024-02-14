class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Initialise variables and starting conditions
        n = len(nums)
        half = int(n / 2)
        positive_nums = []
        negative_nums = []
        for num in nums:
            if num >= 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)
        for i in range(0, half):
            nums[2 * i] = positive_nums[i]
            nums[2 * i + 1] = negative_nums[i]
        return nums
