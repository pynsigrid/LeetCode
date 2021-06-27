from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, TreeNode):
        def dfs(bt, in_order):
            if not bt: return
            print(in_order)
            dfs(bt.left, in_order)
            in_order.append(bt.val)
            dfs(bt.right, in_order)
            return 
        in_order = []
#         bt = TreeNode
        dfs(TreeNode, in_order)
        return in_order
    

def main():
    
    bt1 = TreeNode(1, None, None)
    bt2 = TreeNode(2, None, None)
    bt3 = TreeNode(3, None, None)
    bt4 = TreeNode(4, None, None)
    bt5 = TreeNode(5, None, None)
    bt6 = TreeNode(6, None, None)
    bt7 = TreeNode(7, None, None)

    bt1.left, bt1.right = bt2, bt3
    bt2.left, bt2.right = bt4, bt5
    bt3.left, bt3.right = bt6, bt7

    a = Solution()
    res = a.inorderTraversal(bt1)
    print(res)

if __name__ == '__main__':
    main()
