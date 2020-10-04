# LeetCode_LearningPath
this is the leetcode script
👇这些为了打卡而没有做题的日子
20200914
20200916
from pepper

20201003
# 237. 删除链表中的结点
input是node不是node.val，所以将next的结点覆盖前一结点，前一结点的指针指向下下一个点上
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

20201004
# 237. 删除链表中的结点
input是node不是node.val，所以将next的结点覆盖前一结点，前一结点的指针指向下下一个点上
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
