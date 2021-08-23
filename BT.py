from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(6)
t2 = TreeNode(2)
t3 = TreeNode(8)
t4 = TreeNode(0)
t5 = TreeNode(4)
t6 = TreeNode(7)
t7 = TreeNode(9)
t8 = TreeNode(3)
t9 = TreeNode(5)

t1.left, t1.right = t2, t3
t2.left, t2.right = t4, t5
t3.left, t3.right = t6, t7
t5.left, t5.right = t8, t9

# bt6.left = bt8

class Solution:
    def lowestCommonAncestor(self, \
    root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return
            if node.val>p.val and node.val>q.val:
                return dfs(node.left)  # 记录上一个返回的节点，即最近公共祖先
            elif node.val<p.val and node.val<q.val:
                return dfs(node.right)
            return node  
        return dfs(root)


a = Solution()
res = a.lowestCommonAncestor(t1, t8, t9)
print(res.val)