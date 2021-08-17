from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = []
        tmp = []
        def dfs(i, j):
            if i>=m or j>=n:
#                 if i==m and j==n:
                s = sum(tmp)
                res.append(s)
                return
            for row in range(i, m):
                for col in range(j, n):
                    
                    tmp.append(grid[row][col])
                    if row<m:
                        row += 1
                        left = dfs(row, col)
                        tmp.pop()
                        row -= 1

                    if col<n:
                        col += 1
                        down = dfs(row, col)
                        tmp.pop()
                        col -= 1
#                     return
            return res
        return dfs(0, 0)

grid = [[1,3,1],[1,5,1],[4,2,1]]
a = Solution()
res = a.maxValue(grid)
print(res)