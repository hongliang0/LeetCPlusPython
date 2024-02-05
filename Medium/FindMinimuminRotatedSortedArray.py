class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = len(nums) - 1
        start = 0
        smallest = float('inf')
        while start != end:
            # Find the middle floor element
            middle = (start + end) // 2

            # If middle is smaller then middle - 1, answer found
            if (middle - 1) >= 0 and nums[middle - 1] > nums[middle]:
                return nums[middle]
            elif (middle + 1) <= len(nums) - 1 and nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            # If middle is smaller then end, nothing from middle to end can be correct
            elif nums[middle] < nums[end]:
                end = middle

            # If middle number is larger then end, change start
            elif nums[middle] > nums[end]:
                start = middle

        return nums[start]
