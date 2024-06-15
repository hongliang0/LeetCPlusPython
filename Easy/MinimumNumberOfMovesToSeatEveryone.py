class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        moves = 0
        for i in range(len(students)):
            moves += abs(seats[i] - students[i])
        return moves
