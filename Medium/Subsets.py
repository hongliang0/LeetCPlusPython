class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        num_elements = len(nums)
        total_subsets = 1 << num_elements

        for subset_id in range(total_subsets):
            current_subset = []
            for element_index in range(num_elements):
                if subset_id & (1 << element_index):
                    current_subset.append(nums[element_index])
            subsets.append(current_subset)

        return subsets
