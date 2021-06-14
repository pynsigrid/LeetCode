class Solution:
    def combine(self, n, k):
        res, tmp = [], []
        def addElement(n, k, idx):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(idx, n-k+2):
                print(f'i = {i}')
                tmp.append(i)
                addElement(n, k, i+1)
                tmp.pop()
        addElement(n, k, 1)
        return res
            
def main():
    a = Solution()
    res = a.combine(4, 2)
    print(res)

if __name__ == '__main__':
    main()