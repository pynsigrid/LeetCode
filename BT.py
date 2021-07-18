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
    def pathSum(self, root: BinaryTree, targetSum: int) -> List[List[int]]:
        if not root: return False
        self.res, tmp = [], []
        def dfs(bt, tmp, targetSum):
            tmp.append(bt.val)
            targetSum -= bt.val
            print(tmp, targetSum)
            if not bt.left and not bt.right:
#                 tmp.append(bt.val)  # 🍓
                if targetSum == 0:
                    self.res.append(tmp.copy())
                return
            if bt.left:
                dfs(bt.left, tmp, targetSum)
                # print(bt.left.val)
                # targetSum += cur
                tmp.pop()
            if bt.right:
                dfs(bt.right, tmp, targetSum)
                # targetSum += bt
                tmp.pop()
        dfs(root, tmp, targetSum)
        return self.res



a = Solution()
res = a.pathSum(bt1, 7)
print(res)