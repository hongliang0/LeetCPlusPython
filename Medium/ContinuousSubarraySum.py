class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Initialize a dictionary to store the remainder and the corresponding index
        remainder_dict = {0: -1}  # To handle cases where the subarray starts from index 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k

            if remainder in remainder_dict:
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                remainder_dict[remainder] = i

        return False
