class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        elif len(bloomDay) == m * k:
            return max(i for i in bloomDay)

        else:
            def check_make(bloomed, bouquets, flowers):
                batches, current = 0, 0
                for i in range(len(bloomed)):
                    if bloomed[i] == -1:
                        current = 0
                    else:
                        current += 1
                    if current == flowers:
                        batches += 1
                        current = 0
                return batches >= bouquets

            binaryset = set()
            for num in bloomDay:
                binaryset.add(num)
            mylist = sorted(list(binaryset))
            left, right = 0, len(mylist) - 1
            while left <= right:
                middle = (left + right) // 2
                bloomed_copy = bloomDay.copy()
                for i in range(len(bloomed_copy)):
                    if bloomed_copy[i] > mylist[middle]:
                        bloomed_copy[i] = -1
                if check_make(bloomed_copy, m, k):
                    right = middle - 1
                else:
                    left = middle + 1

            return mylist[left]
