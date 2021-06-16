from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, tmp = [], []
        csum = 0
        def addElement(candidates, csum):
            if csum == target:
                res.append(tmp[:])
                return
            elif csum > target:
                return
            else:
                for i in candidates:  
                    tmp.append(i)
                    csum += i
                    addElement(candidates, csum)
                    candidates = candidates[1:]
                    tmp.pop()
                    csum -= i
        
        addElement(candidates, 0)
        return res

def main():
    
    candidates = [2,3,5]
    target = 8

    a = Solution()
    res = a.combinationSum(candidates, target)
    print(res)

if __name__ == '__main__':
    main()
