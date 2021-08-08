from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res, tmp = [], []
        s = targetSum
        def dfs(node, tmp, s):
            if not node.left and not node.right:
                # tmp.append(
                    
                print(s, node.val)
                if s == 0: 
                    print(tmp)
                    res.append(tmp.copy())
                return
            # tmp.append(node.val)
            # s -= node.val
#             print(node.val)
            if node.left:
                tmp.append(node.left.val)
                s -= node.left.val
                left = dfs(node.left, tmp, s)
                tmp.pop()
                s += node.left.val
            if node.right:
                tmp.append(node.right.val)
                s -= node.right.val

                right = dfs(node.right, tmp, s)
                tmp.pop()
                s += node.right.val
            # 需要遍历所有路径，所以不需要有返回值
            return res
        if not root: return []
        tmp.append(root.val)
        return dfs(root, tmp, s-root.val)

def main():
    
    bt1 = TreeNode(1, None, None)
    bt2 = TreeNode(2, None, None)
    bt3 = TreeNode(3, None, None)
    bt4 = TreeNode(4, None, None)
    bt5 = TreeNode(5, None, None)
    bt6 = TreeNode(6, None, None)
    bt7 = TreeNode(3, None, None)

    bt1.left, bt1.right = bt2, bt3
    bt2.left, bt2.right = bt4, bt5
    bt3.left, bt3.right = bt6, bt7

    a = Solution()
    res = a.pathSum(bt1, 7)
    print(res)

if __name__ == '__main__':
    main()
