# class Solution(object):
    
#     def exchange(self, nums):
#         res, tmp = [], []
#         def recursion(n):
#             if n <= 1:
#                 tmp = ['()']
#                 return ['()']
                
#             # r = recursion(n-1)
#             # print(r)
#             for i in recursion(n-1):
#                 res.append('('+i+')')
#                 res.append('()'+i)
#                 res.append(i+'()')
#             return res
#         return recursion(nums)

# a = Solution()
# res = a.exchange(3)
# print(res)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 终止条件
        if head == None or head.next == None: return head
        cur = self.reverseList(head.next)  # 最终找到新的头节点
        print(head.val, cur.val)
        head.next.next = head
        head.next = None
        return cur

l1, l2 = ListNode(1), ListNode(2)
l3, l4 = ListNode(3), ListNode(4)
l5, l6 = ListNode(5), ListNode(6)
# l1
l5.next = l6
l4.next = l5
l3.next = l4
l2.next = l3
l1.next = l2


a = Solution()
res = a.reverseList(l1)
print(l1.next.next.val)