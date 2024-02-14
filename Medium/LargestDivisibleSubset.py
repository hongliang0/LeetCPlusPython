class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort nums from smallest to largest
        nums.sort()
        # Prepare variables
        # dp keeps track of subset count, subset keeps track of subset list
        dp = [1] * len(nums)
        subset = [[] for _ in range(len(nums))]
        max_size = 1
        max_index = 0
        # Loop through nums
        for i in range(len(nums)):
            subset[i].append(nums[i])
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        subset[i] = list(subset[j])
                        subset[i].append(nums[i])
                        # print(f"{nums[i]} has subset of {subset[i]}")
                    # print(f"{nums[i]} and {nums[j]} equals division {nums[i] % nums[j]}")
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i
        # Return the solution
        return subset[max_index]
