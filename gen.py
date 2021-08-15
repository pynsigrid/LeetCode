# class Solution(object):
    
#     def exchange(self, nums):
#         res, tmp = [], []
#         def recursion(n):
#             if n <= 1:
#                 tmp = ['()']
#                 return ['()']
                
#             # r = recursion(n-1)
#             # print(r)
#             for i in recursion(n-1):
#                 res.append('('+i+')')
#                 res.append('()'+i)
#                 res.append(i+'()')
#             return res
#         return recursion(nums)

# a = Solution()
# res = a.exchange(3)
# print(res)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l, r):
            if not l and not r: return True
            if not l or not r or l.val!=r.val: return False
            # if l.left and r.right:
            #     if dfs(l.left, r.right): 
            #         return True
            #     else:
            #         return False
            # if l.right and r.left:
            #     if dfs(l.right, r.left): 
            #         return True
            #     else:
            #         return False
            # # return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        if not root: return True
        return dfs(root.left, root.right)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(2)
t4 = TreeNode(3)
t5 = TreeNode(4)
t6 = TreeNode(4)
t7 = TreeNode(3)
t1.left, t1.right = t2, t3
t2.left, t2.right = t4, t5
t3.left, t3.right = t6, t7

a = Solution()
res = a.isSymmetric(t1)
print(res)
# res.left.right.val