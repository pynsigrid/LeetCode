class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dsum(i):
            n = 0
            while i:
                n += i%10
                i //= 10
            return n
        def dfs(i, j, k):
            
            if i>=m or i<0 or j>=n or j<0 \
                or dsum(i)+dsum(j)>k or (i,j) in used:
                return 0
            used.add((i, j))
            print(used)
            res = 1+max(dfs(i+1,j,k), dfs(i-1,j,k), dfs(i,j-1,k), dfs(i,j+1,k))
            # used.pop()
            return res
        used = set()
        return dfs(0,0,k)

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

a = Solution()
res = a.movingCount(3,6,5)
print(res)