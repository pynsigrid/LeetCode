from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, tmp = [], []
        used = [False for _ in range(len(candidates))]
        csum = 0
        idx = 0
        def addElement(candidates, csum, idx, used):
            if csum == target: return res.append(tmp.copy())
            if csum > target: return 
            for i in range(idx, len(candidates)):
                # 剪枝
                # if candidates[i]+csum > target: return
                # 去重
                if i>0 and candidates[i]==candidates[i-1] and not used[i]: 
                    continue
                tmp.append(candidates[i])
                csum += candidates[i]
                used[i] = True
                addElement(candidates, csum, i+1, used)
                tmp.pop()
                csum -= candidates[i]
                used[i] = False
        candidates.sort()
        addElement(candidates, 0, 0, used)
        return res

def main():
    
    candidates = [10,1,2,7,6,1,5]
    target = 8

    a = Solution()
    res = a.combinationSum2(candidates, target)
    print(res)

if __name__ == '__main__':
    main()
