from typing import List
class BinaryTree():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

bt1 = BinaryTree(1, None, None)
bt2 = BinaryTree(2, None, None)
bt3 = BinaryTree(3, None, None)
bt4 = BinaryTree(4, None, None)
bt5 = BinaryTree(5, None, None)
bt6 = BinaryTree(3, None, None)
bt7 = BinaryTree(7, None, None)
bt8 = BinaryTree(8, None, None)

bt1.left, bt1.right = bt2, bt3
bt2.left = bt4
bt3.left = bt6

# bt6.left = bt8

class Solution:
    def pathSum(self, root: BinaryTree, target: int) -> List[List[int]]:
        def dfs(node, target):
            if not node.left and not node.right:
                if target == 0:
                    res.append(tmp.copy())
                return res
            if target < 0: return
            if node.left:
                tmp.append(node.left.val)
                dfs(node.left, target-node.left.val)
                tmp.pop()
            if node.right:
                tmp.append(node.right.val)
                dfs(node.right, target-node.right.val)
                tmp.pop()
            return res
        if not root: return []
        res, tmp = [], []
        tmp.append(root.val)
        return dfs(root, target-root.val)


a = Solution()
res = a.pathSum(bt1, 7)
print(res)