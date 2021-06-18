from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, tmp = [],[]
        csum, idx = 10000, 0
        def addElement(idx):
            if csum == n and len(tmp) == k: return res.append(tmp.copy())
            if csum > n or len(tmp) > k: return  # pruning
            for i in range(idx, 10):
                tmp.append(i)
                csum += i
                addElement(i+1)
                tmp.pop()
                csum -= i
        addElement(1)
        return res

def main():

    a = Solution()
    res = a.combinationSum3(3, 9)
    print(res)

if __name__ == '__main__':
    main()
