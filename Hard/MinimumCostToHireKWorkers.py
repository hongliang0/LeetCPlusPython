class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        my_dict = {}
        for i in range(len(quality)):
            my_dict[wage[i]] = [wage[i], quality[i], quality[i] / wage[i]]
        sorted_dict = list(sorted(my_dict.items(), key=lambda x: x[1][2]))
        hired_workers = []
        for i in range(k, 0, -1):
            hired_workers.append(sorted_dict[k])
        print(hired_workers)
        return 0
