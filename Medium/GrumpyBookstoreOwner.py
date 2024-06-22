class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                happy += customers[i]
                customers[i] = 0
        max_happy = sum(customers[0:minutes])
        current_happy = max_happy
        for i in range(minutes, len(customers)):
            current_happy += customers[i] - customers[i - minutes]
            max_happy = max(max_happy, current_happy)
        return happy + max_happy
