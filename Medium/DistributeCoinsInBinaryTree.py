# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def distributeCoins(self, root: TreeNode) -> int:
#         self.moves = 0

#         def postOrder(node):
#             if not node:
#                 return 0

#             left_balance = postOrder(node.left)
#             right_balance = postOrder(node.right)

#             # Total moves to balance the current node with its children
#             self.moves += abs(left_balance) + abs(right_balance)

#             # Returning the balance of coins for the current node
#             return node.val + left_balance + right_balance - 1

#         postOrder(root)
#         return self.moves

#    1
#  0   0
#   3

class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0

            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            self.moves += abs(left_balance) + abs(right_balance)

            return node.val + left_balance + right_balance - 1

        dfs(root)
        return self.moves
