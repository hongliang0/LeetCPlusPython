class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_dict = {0: 1}
        current_sum = 0
        counter = 0

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            # Normalize the remainder to be positive
            if remainder < 0:
                remainder += k

            if remainder in remainder_dict:
                counter += remainder_dict[remainder]
                remainder_dict[remainder] += 1
            else:
                remainder_dict[remainder] = 1

        return counter
