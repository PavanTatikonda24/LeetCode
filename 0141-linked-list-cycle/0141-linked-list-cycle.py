# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        index=[]
        index.insert(-1,head)
        while head and head.next:
            head=head.next
            if head in index:
                return True
            else:
                index.insert(-1,head)


        