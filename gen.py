class Solution:
    def exist(self, board, word):
        def dfs(idx, i, j):
            
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[idx]:
                return False
            if idx==len(word)-1:  # 🍓
                return True
            tmp, board[i][j] = board[i][j], '-1' 
            res = dfs(idx+1, i+1, j) or dfs(idx+1, i-1, j) or dfs(idx+1, i, j+1) or dfs(idx+1, i, j-1)
            board[i][j] = tmp
            return res
        if not word: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

a = Solution()
res = a.exist(board, word)
print(res)