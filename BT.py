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

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if p.val<=node.val<=q.val or q.val<=node.val<=p.val:
                return node
            elif node.val>p.val and node.val>q.val:
                res = dfs(node.left)
                return res
            elif node.val<p.val and node.val<q.val:
                res = dfs(node.right)
                return res
            # else:
            #     return False
            # return res
        return dfs(root)


a = Solution()
res = a.lowestCommonAncestor(t1, t8, t9)
print(res.val)