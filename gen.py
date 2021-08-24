class Solution:
    def strStr(self, haystack, needle):
        H, N = len(haystack), len(needle)
        if not N: return 0
        
        p1 = 0
        while p1 < H:
            print(p1)
            if haystack[p1] != needle[0]:
                p1 += 1
            else:
                start_match = p1
                p2 = 0
                while p2 < N:
                    print(p1, p2, haystack[start_match:p2+1])
                    if haystack[p1] != needle[p2]:
                        p1 = start_match+1
                        break
                    elif p2-start_match+1 == N:
                        return start_match
                    else:
                        p1 += 1
                        p2 += 1
        return -1

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

haystack = "mississippi"
needle = "issip"
a = Solution()
res = a.strStr(haystack, needle)
print(res)