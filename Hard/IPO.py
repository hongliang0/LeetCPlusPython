class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: x[1])
        pointer, completed = 0, 0

        my_heap = []
        heapq.heapify(my_heap)

        while completed < k:
            while pointer < len(profits) and projects[pointer][1] <= w:
                heapq.heappush(my_heap, -projects[pointer][0])
                pointer += 1
            if my_heap:
                w -= heapq.heappop(my_heap)
                completed += 1
            else:
                break
        return w
