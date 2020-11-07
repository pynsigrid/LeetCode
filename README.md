# LeetCode_LearningPath
this is the leetcode script
👇这些为了打卡而没有做题的日子
20200914
20200916
20201017
from pepper

24. 两两交换链表的节点
1）递归 t:O(n),s:O(n)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
2）迭代 t:O(n),s:O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next
