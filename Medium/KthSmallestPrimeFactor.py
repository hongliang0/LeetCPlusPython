class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        my_dict = {}
        new_arr = []
        for i in range(n):
            for j in range(i, n):
                new_arr.append(arr[i] / arr[j])
                my_dict[arr[i] / arr[j]] = [arr[i], arr[j]]
        new_arr.sort()
        return my_dict[new_arr[k - 1]]
