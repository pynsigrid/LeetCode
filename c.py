from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2letter={0:'', 1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        num2letter={'0':'', '1':'', '2':'abc', '3':'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        res, tmp = [], []
        idx = 0
        def addElement(digits, idx):
            print(idx, digits[idx])
            if idx >= len(digits):
#             if len(tmp) == len(digits):
                res.append(''.join(tmp))
                return 
            letter = num2letter[str(digits[idx])]
            for i in letter:
                tmp.append(i)
                addElement(digits, idx+1)
                tmp.pop()
                idx -= 1
        addElement(digits, 0)
        return res

def main():
    a = Solution()
    res = a.letterCombinations('23')
    print(res)

if __name__ == '__main__':
    main()