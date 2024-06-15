class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        while hand:
            first = min(hand)
            for i in range(groupSize):
                if first + i in hand:
                    hand.remove(first + i)
                else:
                    return False
        return True
