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


class Solution:
    def isSubStructure(self, A, B):
        def treeMatch(A, B):
            if not B: return True
            if not A or A.val!=B.val: return False
            return treeMatch(A.left, B.left) and treeMatch(A.right, B.right)
        
        def treeIncludeSub(A, B):
            if not A: return False
            if A.val==B.val: 
                if treeMatch(A, B): return True
            if A.left:
                if treeIncludeSub(A.left, B): return True
            if A.right:
                if treeIncludeSub(A.right, B): return True
            # return False
        if not B: return False
        return treeIncludeSub(A, B)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSubStructure(self, A, B):
#         def recur(A, B):
#             if not B: return True
#             if not A or A.val != B.val: return False
#             return recur(A.left, B.left) and recur(A.right, B.right)

#         return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


t1 = TreeNode(3)
t2 = TreeNode(4)
t3 = TreeNode(5)
t4 = TreeNode(1)
t5 = TreeNode(2)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

b1 = TreeNode(5)
# b2 = TreeNode(1)
# b1.left = b2

a = Solution()
res = a.isSubStructure(t1, b1)
print(res)