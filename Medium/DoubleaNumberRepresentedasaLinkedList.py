# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        # Do maths here
        reverse_head = prev
        current = prev
        carry = 0
        while current:
            if current.val * 2 + carry >= 10:
                current.val = (current.val * 2 + carry) % 10
                carry = 1
            else:
                current.val = current.val * 2 + carry
                carry = 0
            if not current.next and carry == 1:
                current.next = ListNode(1)
                break
            current = current.next

        # Unreversed list
        prev = None
        current = reverse_head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
