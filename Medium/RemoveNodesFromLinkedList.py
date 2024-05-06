# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        # New Reversed list
        reverse_head = prev
        current = prev
        local_max = current.val
        while current.next:
            if current.next.val < local_max:
                current.next = current.next.next
            else:
                current = current.next
                local_max = max(local_max, current.val)

        # ReReversed list
        prev = None
        current = reverse_head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
