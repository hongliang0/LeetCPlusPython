/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func removeNodes(_ head: ListNode?) -> ListNode? {
        // Corner Case
        guard let head = head else { return nil }

        // Reverse the list
        var prev: ListNode? = nil
        var current = head

        while let next = current.next {
            current.next = prev
            prev = current
            current = next
        }
        current.next = prev

        // Reversed List: Discard unwanted
        var newHead = current
        var localMax = newHead.val
        var currentNode = newHead

        while let nextNode = currentNode.next {
            if nextNode.val < localMax {
                currentNode.next = nextNode.next
            } else {
                localMax = max(localMax, nextNode.val)
                currentNode = nextNode
            }
        }

        // Reverse the list and return
        prev = nil
        current = newHead
        while let next = current.next {
            current.next = prev
            prev = current
            current = next
        }
        current.next = prev
        return current
    }
}