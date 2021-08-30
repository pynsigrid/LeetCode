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
    def permutation(self, s: str) -> List[str]:
        def backtrack(tmp, usd):
            if len(usd)==len(s): 
                res.append(''.join(tmp))
                return
            for i in s:
                if i in usd: continue
                tmp.append(i)
                usd.append(i)
                backtrack(tmp, usd)
                tmp.pop()
                usd.pop()

        if not s: return []
        res, tmp, usd = [], [], []
        backtrack(tmp, usd)
        return res
                


s = "abc"
a = Solution()
res = a.permutation(s)

print(res)