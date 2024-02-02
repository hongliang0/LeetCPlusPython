class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        divided_array = []
        nums.sort()
        # Declare variables before use
        last_num = nums[0]
        temp_array = []
        for num in nums:
            # If there is no temp_array or a new one needs to be created
            if not temp_array or len(temp_array) == 3:
                temp_array = []
                last_num = num
            # If the difference is too big, return empty array
            if num - last_num > k:
                # print(f"Difference of {num - last_num} in {num} and {last_num}")
                return []
            temp_array.append(num)
            # If temp_array has reached size 3, add to divided_array answer
            if len(temp_array) == 3:
                divided_array.append(temp_array)
        return divided_array
